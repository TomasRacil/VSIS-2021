import { useState } from "react";

const AddUtvar = () => {
  const [nazev_utvaru, setNazevUtvaru] = useState("Univerzita Obrany");
  const [lokace, setLokace] = useState("Brno");
  const [cislo_vu, setCisloVU] = useState("2994");

  const handleSubmit = (e) => {
    e.preventDefault();
    const utvar = { nazev_utvaru, lokace, cislo_vu };
    fetch("/api/utvar/", {
      method: "POST",
      headers: {
        "Content-type": "application/json; charset=UTF-8", // Indicates the content
      },
      body: JSON.stringify(utvar),
    }).then((res) => {
      console.log("New utvar added");
      console.log(res);
    });
  };

  return (
    <div className="create">
      <h2>Add new utvar</h2>
      <form onSubmit={handleSubmit}>
        <label>Název útvaru:</label>
        <input
          type="text" 
          value={nazev_utvaru}
          onChange={(e) => setNazevUtvaru(e.target.value)}
        />
        <label>Lokace:</label>
        <input
          type="text"
          required
          value={lokace}
          onChange={(e) => setLokace(e.target.value)}
        />
        <label>Číslo VÚ:</label>
        <input
          type="text" //number
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
