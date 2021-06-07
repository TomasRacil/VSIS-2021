import { useState } from "react";

const AddUtvar = () => {
  const [nazev_utvaru, setNazevUtvaru] = useState("email");
  const [lokace, setLokace] = useState("username");
  const [cislo_vu, setCisloVU] = useState("password");

//   const handleSubmit = (e) => {
//     e.preventDefault();
//     const user = { email, username, password };
//     fetch("/api/user/", {
//       method: "POST",
//       headers: {
//         "Content-type": "application/json; charset=UTF-8", // Indicates the content
//       },
//       body: JSON.stringify(user),
//     }).then((res) => {
//       console.log("New user added");
//       console.log(res);
//     });
//   };

  return (
    <div className="create">
      <h2>Add new user</h2>
      <form onSubmit={handleSubmit}>
        <label>nazev utvaru:</label>
        <input
          type="text"
          required
          value={nazev_utvaru}
          onChange={(e) => setNazevUtvaru(e.target.value)}
        />
        <label>lokace:</label>
        <input
          type="text"
          required
          value={lokace}
          onChange={(e) => setLokace(e.target.value)}
        />
        <label>cislo VU:</label>
        <input
          type="text"
          required
          value={cislo_vu}
          onChange={(e) => setCisloVU(e.target.value)}
        />
        <button>Register</button>
        <p>{nazev_utvaru}</p>
        <p>{lokace}</p>
        <p>{cislo_vu}</p>
      </form>
    </div>
  );
};

export default AddUtvar;
