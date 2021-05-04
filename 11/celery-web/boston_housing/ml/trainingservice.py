import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Input
from .datahelper import prepare_datasets
from celery.utils.log import get_task_logger

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)

def build_model(columns_len):
    # Define model layers.
    input_layer = Input(shape=(columns_len,))
    first_dense = Dense(units='128', activation='relu')(input_layer)
    # Y1 output will be fed from the first dense
    y1_output = Dense(units='1', name='price_output')(first_dense)

    second_dense = Dense(units='128', activation='relu')(first_dense)
    # Y2 output will be fed from the second dense
    y2_output = Dense(units='1', name='ptratio_output')(second_dense)

    # Define the model with the input layer and a list of output layers
    model = Model(inputs=input_layer, outputs=[y1_output, y2_output])

    return model

def run_training(dataset_split):
    norm_train_X, norm_test_X, norm_val_X, train_Y, test_Y, val_Y = prepare_datasets(dataset_split)
    celery_log.info(f"Data prepared")

    model = build_model(len(norm_train_X[0]))

    # Specify the optimizer, and compile the model with loss functions for both outputs
    optimizer = tf.keras.optimizers.SGD(lr=0.001)
    model.compile(optimizer=optimizer,
                  loss={'price_output': 'mse', 'ptratio_output': 'mse'},
                  metrics={'price_output': tf.keras.metrics.RootMeanSquaredError(),
                           'ptratio_output': tf.keras.metrics.RootMeanSquaredError()})

    # Train the model for 100 epochs
    model.fit(norm_train_X, train_Y,
              epochs=1000, batch_size=10,
              validation_data=(norm_test_X, test_Y),
              verbose=0)

    # Test the model and print loss and rmse for both outputs
    loss, Y1_loss, Y2_loss, Y1_rmse, Y2_rmse = model.evaluate(x=norm_val_X, y=val_Y)

    celery_log.info(f'loss: {loss}')
    celery_log.info(f'price_loss: {Y1_loss}')
    celery_log.info(f'ptratio_loss: {Y2_loss}')
    celery_log.info(f'price_rmse: {Y1_rmse}')
    celery_log.info(f'ptratio_rmse: {Y2_rmse}')

    celery_log.info('Training task completed')
    # Run predict
    Y_pred = model.predict(norm_test_X)
    price_pred = Y_pred[0]
    ptratio_pred = Y_pred[1]
    celery_log.info('Predict task completed')