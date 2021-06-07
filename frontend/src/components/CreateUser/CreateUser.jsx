import { useState } from "react";

const CreateUser = () => {
  const [email, setEmail] = useState("email");
  const [username, setUsername] = useState("username");
  const [password, setPassword] = useState("password");
  const [password2, setPassword2] = useState("password2");

  const handleSubmit = (e) => {
    e.preventDefault();
    const user = { email, username, password };
    fetch("/api/user/", {
      method: "POST",
      headers: {
        "Content-type": "application/json; charset=UTF-8", // Indicates the content
      },
      body: JSON.stringify(user),
    }).then((res) => {
      console.log("New user added");
      console.log(res);
    });
  };

  return (
    <div className="create">
      <h2>Add new user</h2>
      <form onSubmit={handleSubmit}>
        <label>Email:</label>
        <input
          type="text"
          required
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <label>Username:</label>
        <input
          type="text"
          required
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <label>Password:</label>
        <input
          type="password"
          required
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <label>Retype password:</label>
        <input
          type="password"
          required
          value={password2}
          onChange={(e) => setPassword2(e.target.value)}
        />
        <button>Register</button>
        <p>{email}</p>
        <p>{username}</p>
        <p>{password}</p>
        <p>{password2}</p>
        {password !== password2 && <p>Hesla se neshoduji</p>}
      </form>
    </div>
  );
};

export default CreateUser;
