import * as tf from "@tensorflow/tfjs";

export function prepareData() {
    let data = [];

    const redData1 = { xs: [150, 200], ys: 'Red' };
    const redData2 = { xs: [150, 400], ys: 'Red' };
    const redData3 = { xs: [200, 250], ys: 'Red' };
    const redData4 = { xs: [250, 150], ys: 'Red' };
    const redData5 = { xs: [250, 350], ys: 'Red' };
    const redData6 = { xs: [300, 300], ys: 'Red' };

    const greenData1 = { xs: [500, 700], ys: 'Green' };
    const greenData2 = { xs: [550, 800], ys: 'Green' };
    const greenData3 = { xs: [550, 900], ys: 'Green' };
    const greenData4 = { xs: [600, 700], ys: 'Green' };
    const greenData5 = { xs: [600, 750], ys: 'Green' };
    const greenData6 = { xs: [650, 850], ys: 'Green' };

    const blueData1 = { xs: [800, 200], ys: 'Blue' };
    const blueData2 = { xs: [850, 100], ys: 'Blue' };
    const blueData3 = { xs: [850, 400], ys: 'Blue' };
    const blueData4 = { xs: [900, 200], ys: 'Blue' };
    const blueData5 = { xs: [900, 250], ys: 'Blue' };
    const blueData6 = { xs: [950, 200], ys: 'Blue' };

    data.push(redData1);
    data.push(redData2);
    data.push(redData3);
    data.push(redData4);
    data.push(redData5);
    data.push(redData6);

    data.push(greenData1);
    data.push(greenData2);
    data.push(greenData3);
    data.push(greenData4);
    data.push(greenData5);
    data.push(greenData6);

    data.push(blueData1);
    data.push(blueData2);
    data.push(blueData3);
    data.push(blueData4);
    data.push(blueData5);
    data.push(blueData6);

    data.forEach(function (item, index) {
        item.xs[0] = (item.xs[0] / (1000 / 2)) - 1;
        item.xs[1] = (item.xs[1] / (1000 / 2)) - 1;
    })

    console.log('Data size: ' + data.length);
    console.log(data);
    const training_size = Math.round((data.length * 80) / 100);

    const dataShuffled = tf.data.array(data).shuffle(3);

    const dataTraining = dataShuffled.take(training_size);
    const dataValidation = dataShuffled.skip(training_size);

    const convertedDataTraining =
        dataTraining.map(({ xs, ys }) => {
            const labels = [
                ys == "Red" ? 1 : 0,
                ys == "Green" ? 1 : 0,
                ys == "Blue" ? 1 : 0
            ]
            return { xs: Object.values(xs), ys: Object.values(labels) };
        }).batch(1);

    const convertedDataValidation =
        dataValidation.map(({ xs, ys }) => {
            const labels = [
                ys == "Red" ? 1 : 0,
                ys == "Green" ? 1 : 0,
                ys == "Blue" ? 1 : 0
            ]
            return { xs: Object.values(xs), ys: Object.values(labels) };
        }).batch(1);

    const numOfFeatures = 2;

    return [numOfFeatures, convertedDataTraining, convertedDataValidation];
}