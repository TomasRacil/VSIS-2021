import { useState } from "react";

const AddKurz = () => {
  const [nazev, setNazev] = useState("Vytváření web. stránek");
  const [misto, setMisto] = useState("Praha");
  const [voj_oznaceni, setVojOznaceni] = useState("S12345");
  const [zacatek_kurzu, setZacatekKurzu] = useState();
  const [konec_kurzu, setKonecKurzu] = useState();
  

  const handleSubmit = (e) => {
    e.preventDefault();
    const kurz = { 
      nazev, 
      misto, 
      voj_oznaceni,
      zacatek_kurzu,
      konec_kurzu, 
    };
    fetch("/api/kurz/", {
      method: "POST",
      headers: {
        "Content-type": "application/json; charset=UTF-8", // Indicates the content
      },
      body: JSON.stringify(kurz),
    }).then((res) => {
      console.log("New kurz added");
      console.log(res);
    });
  };

  return (
    <div className="create">
      <h2>Add new kurz</h2>
      <form onSubmit={handleSubmit}>
        <label>Název kurzu:</label>
        <input
          type="text"
          value={nazev}
          onChange={(e) => setNazev(e.target.value)}
        />
        <label>Místo kurzu:</label>
        <input
          type="text"
          required
          value={misto}
          onChange={(e) => setMisto(e.target.value)}
        />
        <label>Vojenské označení:</label>
        <input
          type="text" 
          required
          value={voj_oznaceni}
          onChange={(e) => setVojOznaceni(e.target.value)}
        />
        <label>Začátek kurzu:</label>
        <input
          type="date" 
          required
          value={zacatek_kurzu}
          onChange={(e) => setZacatekKurzu(e.target.value)}
        />
        <label>Konec kurzu:</label>
        <input
          type="date" 
          required
          value={konec_kurzu}
          onChange={(e) => setKonecKurzu(e.target.value)}
        />
        <button>Register</button>
        <p>{nazev}</p>
        <p>{misto}</p>
        <p>{voj_oznaceni}</p>
        <p>{zacatek_kurzu}</p>
        <p>{konec_kurzu}</p>
      </form>
    </div>
  );
};

export default AddKurz;