import { useState } from "react";

const AddHodnost = () => {
  const [nazev, setNazev] = useState("Vojín");
  const [hodnostni_sbor, setHodnostniSbor] = useState("Mužstvo");

  const handleSubmit = (e) => {
    e.preventDefault();
    const hodnost = { nazev, hodnostni_sbor };
    fetch("/api/hodnost/", {
      method: "POST",
      headers: {
        "Content-type": "application/json; charset=UTF-8", // Indicates the content
      },
      body: JSON.stringify(hodnost),
    }).then((res) => {
      console.log("New hodnost added");
      console.log(res);
    });
  };

  return (
    <div className="create">
      <h2>Add new hodnost</h2>
      <form onSubmit={handleSubmit}>
        <label>Název hodnosti:</label>
        <input
          type="text"
          required
          value={nazev}
          onChange={(e) => setNazev(e.target.value)}
        />
        <label>Hodnostní sbor:</label>
        <input
          type="text"
          required
          value={hodnostni_sbor}
          onChange={(e) => setHodnostniSbor(e.target.value)}
        />
        <button>Register</button>
        <p>{nazev}</p>
        <p>{hodnostni_sbor}</p>
      </form>
    </div>
  );
};

export default AddHodnost;