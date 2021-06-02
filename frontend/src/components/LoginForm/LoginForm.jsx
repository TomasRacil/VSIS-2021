import { Component } from "react";

class LoginForm extends Component {
  state = {};

  handleSubmit() {
    console.log("submit");
  }

  render() {
    return (
      <div className="Login">
        <form>
          <label for="email">
            <b>Email</b>
          </label>
          <input type="email" placeholder="Enter email" name="email" required />
          <label for="password">
            <b>Password</b>
          </label>
          <input
            type="password"
            placeholder="Enter password"
            name="password"
            required
          />
          <button type="submit">Login</button>
          <label>
            <input type="checkbox" checked="checked" name="remember" />
          </label>
        </form>
      </div>
    );
  }
}

export default LoginForm;
