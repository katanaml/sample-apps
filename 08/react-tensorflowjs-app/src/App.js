import logo from './logo.svg';
import './App.css';
import * as tf from '@tensorflow/tfjs';
import { prepareData } from "./dataHelper";
import { runTraining } from "./modelTraining";

const handleRunTraining = async (event) => {
  const [numOfFeatures, convertedDataTraining, convertedDataValidation] = prepareData();

  console.log('Training data:');
  await convertedDataTraining.forEachAsync(e => console.log(e));

  await runTraining(numOfFeatures, convertedDataTraining, convertedDataValidation);
};

const handleRunInference = async (event) => {
  const model = await tf.loadLayersModel('indexeddb://basic-model');

  let data = [700, 300];
  data[0] = (data[0] / (1000 / 2)) - 1;
  data[1] = (data[1] / (1000 / 2)) - 1;

  const input = tf.tensor2d(data, [1, data.length]);
  const prediction = model.predict(input);

  const pIndex = tf.argMax(prediction, 1).dataSync();
  const classNames = ["Red", "Green", "Blue"];
  const probability = prediction.dataSync()[pIndex];
  const result = classNames[pIndex];

  prediction.dispose();

  console.log(result + ' : ' + probability);
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <br />
        <table>
          <tbody>
            <tr>
              <th>
                <button onClick={handleRunTraining}>Run training</button>
              </th>
              <th>
                <button onClick={handleRunInference}>Run inference</button>
              </th>
            </tr>
          </tbody>
        </table>
      </header>
    </div>
  );
}

export default App;
