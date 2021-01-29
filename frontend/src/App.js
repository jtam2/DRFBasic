import axios from 'axios';
import './App.css';

function App() {
  const onCLick = async () => {
    console.log('HELLO WORD')
    try {
      await axios.post('http://ec2-52-40-148-210.us-west-2.compute.amazonaws.com:8000/basic/')
    } catch(e){
      console.log(e)
    }

  }
  return (
    <div className="App">
      <button onClick={onCLick}>HELLO WORLD</button>
    </div>
  );
}

export default App;
