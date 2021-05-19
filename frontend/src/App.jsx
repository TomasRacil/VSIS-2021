import Navbar from "./components/Navbar/Navbar";
import Home from "./components/Home/Home";
import CreateUser from "./components/CreateUser/CreateUser";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import UserDetails from "./components/UserDetails/UserDetails";

function App() {
  // function test() {
  //   fetch("/api/test/")
  //     .then((res) => {
  //       return res.json();
  //     })
  //     .then((data) => console.log(data));
  // }
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="content">
          <Switch>
            <Route exact path="/" children={<Home />} />
            <Route exact path="/register" children={<CreateUser />} />
            <Router exact path="/users/:id">
              <UserDetails />
            </Router>
          </Switch>
        </div>
        {/* <button onClick={test}>Test</button> */}
      </div>
    </Router>
  );
}

export default App;
