import { useState } from "react";

const AddOsoba = () => {
  const [jmeno, setJmeno] = useState("Karel");
  const [prijmeni, setPrijmeni] = useState("Novák");
  const [osobni_cislo, setOsobniCislo] = useState("12312312");

  const handleSubmit = (e) => {
    e.preventDefault();
    const osoba = { jmeno, prijmeni, osobni_cislo };
    fetch("/api/osoba/", {
      method: "POST",
      headers: {
        "Content-type": "application/json; charset=UTF-8", // Indicates the content
      },
      body: JSON.stringify(osoba),
    }).then((res) => {
      console.log("New osoba added");
      console.log(res);
    });
  };

  return (
    <div className="create">
      <h2>Add new osoba</h2>
      <form onSubmit={handleSubmit}>
        <label>Jméno:</label>
        <input
          type="text" //number
          value={jmeno}
          onChange={(e) => setJmeno(e.target.value)}
        />
        <label>Příjmení:</label>
        <input
          type="text"
          required
          value={prijmeni}
          onChange={(e) => setPrijmeni(e.target.value)}
        />
        <label>Osobní číslo:</label>
        <input
          type="number"
          required
          value={osobni_cislo}
          onChange={(e) => setOsobniCislo(e.target.value)}
        />
        <button>Register</button>
        <p>{jmeno}</p>
        <p>{prijmeni}</p>
        <p>{osobni_cislo}</p>
      </form>
    </div>
  );
};

export default AddOsoba;
