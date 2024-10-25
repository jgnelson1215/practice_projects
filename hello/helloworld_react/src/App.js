function App(props) {
  const currDate = new Date();
  
  return (
    <div>
      <h1>Hello world! My name is Julian.</h1>
      <h2>The time and date now is {currDate.toString()}.</h2>
    </div>
  );
}

export default App;
