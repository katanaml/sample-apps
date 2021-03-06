import * as tf from "@tensorflow/tfjs";

function buildModel(numOfFeatures) {
    const model = tf.sequential();

    model.add(tf.layers.dense({
        inputShape: [numOfFeatures],
        units: 12,
        activation: 'relu'
    }));
    model.add(tf.layers.dense({
        units: 3,
        activation: 'softmax'
    }));

    model.compile({ optimizer: tf.train.adam(0.01), loss: 'categoricalCrossentropy', metrics: 'accuracy' });

    return model;
}

export async function runTraining(numOfFeatures, convertedDataTraining, convertedDataValidation) {
    const model = buildModel(numOfFeatures);

    const history = await model.fitDataset(
        convertedDataTraining,
        {
            epochs: 100,
            validationData: convertedDataValidation,
            callbacks: {onEpochEnd: (epoch, logs) => {
                console.log("Epoch: " + epoch + " Loss: " + logs.loss + " Accuracy: " + logs.acc + " Validation loss: " 
                + logs.val_loss + " Validation accuracy: " + logs.val_acc);
             }
        }});

    await model.save('indexeddb://basic-model');
    console.log('Model saved');

    return history;
}