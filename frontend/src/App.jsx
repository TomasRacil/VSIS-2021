import React, { Component } from "react";

async function getMessage() {
  try {
    const res = await fetch("http://172.23.0.1:5000/test");
    const data = await res.json();
    return data;
  } catch (error) {
    return error;
  }
}

class App extends Component {
  //console.log(login("test", "test"))
  componentDidMount() {
    getMessage().then(console.log);
  }

  render() {
    fetch("http://172.23.0.1:5000/user")
      .then((res) => res.json())
      .then(console.log)
      .catch((error) => console.log(error));
    getMessage();
    return <h1>Hello world</h1>;
  }
}

export default App;
