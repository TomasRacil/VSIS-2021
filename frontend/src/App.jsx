import Navbar from "./components/Navbar/Navbar";
import Home from "./components/Home/Home";
import CreateUser from "./components/CreateUser/CreateUser";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import UserDetails from "./components/UserDetails/UserDetails";
import Utvary from "./components/Utvary/Utvary";
import Osoby from "./components/Osoby/Osoby";
import Hodnosti from "./components/Hodnosti/Hodnosti";
import AddUtvar from "./components/Utvary/AddUtvar";

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
            <Route path="/users/:id">
              <UserDetails />
            </Route>
            <Route exact path="/utvary">
              <Utvary></Utvary>
            </Route>
            <Route exact path="/osoby">
              <Osoby></Osoby>
            </Route>
            <Route exact path="/hodnosti">
              <Hodnosti></Hodnosti>
            </Route>
            <Route exact path="/utvary/add">
              <AddUtvar></AddUtvar>
            </Route>
          </Switch>
        </div>
        {/* <Link to="/users/1">User 1</Link> */}
        {/* <button onClick={test}>Test</button> */}
      </div>
    </Router>
  );
}

export default App;
