import { useEffect, useState } from "react";

const AddOsoba = () => {
  const [jmeno, setJmeno] = useState("Karel");
  const [prijmeni, setPrijmeni] = useState("Novák");
  const [osobni_cislo, setOsobniCislo] = useState("12312312");
  const [cislo_vu, setCisloVU] = useState();
  const [utvary, setUtvary] = useState();
  const [hodnosti, setHodnosti] = useState();
  const [nazev, setNazev] = useState();

  const [isPending, setIsPending] = useState(true);
  const [error, setError] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    const osoba = {
      jmeno,
      prijmeni,
      osobni_cislo: parseInt(osobni_cislo),
      utvar: parseInt(cislo_vu),
      hodnost: nazev,
    };
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

  useEffect(() => {
    const abortControler = new AbortController();

    fetch("/api/utvar/", { signal: abortControler.signal })
      .then((res) => {
        if (!res.ok) {
          throw Error("could not fetch the utvary from that source");
        }
        return res.json();
      })
      .then((data) => {
        //console.log(data));
        setUtvary(data.data);
        setIsPending(false);
        setError(null);
      })
      .catch((err) => {
        if (err.name === "AbortError") {
          console.log("fetch aborted");
        } else {
          setIsPending(false);
          setError(err.message);
        }
      });

    return () => abortControler.abort();
  }, []);

  useEffect(() => {
    const abortControler = new AbortController();

    fetch("/api/hodnost/", { signal: abortControler.signal })
      .then((res) => {
        if (!res.ok) {
          throw Error("could not fetch the hodnosti from that source");
        }
        return res.json();
      })
      .then((data) => {
        //console.log(data));
        setHodnosti(data.data);
        setIsPending(false);
        setError(null);
      })
      .catch((err) => {
        if (err.name === "AbortError") {
          console.log("fetch aborted");
        } else {
          setIsPending(false);
          setError(err.message);
        }
      });

    return () => abortControler.abort();
  }, []);

  return (
    <div className="create">
      <h2>Add new osoba</h2>
      <form onSubmit={handleSubmit}>
        <label>Jméno:</label>
        <input
          type="text"
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
        <label>Utvar:</label>
        <select value={cislo_vu} onChange={(e) => setCisloVU(e.target.value)}>
          {error && <option>{error}</option>}
          {isPending && <option>Loading..</option>}
          {utvary &&
            utvary.map((u) => (
              <option key={u.cislo_vu} value={u.cislo_vu}>
                {u.nazev_utvaru}
              </option>
            ))}
        </select>
        <label>Hodnost:</label>
        <select value={nazev} onChange={(e) => setNazev(e.target.value)}>
          {error && <option>{error}</option>}
          {isPending && <option>Loading..</option>}
          {hodnosti &&
            hodnosti.map((u) => (
              <option key={u.nazev} value={u.nazev}>
                {u.nazev}
              </option>
            ))}
        </select>
        <button>Register</button>
        <p>{jmeno}</p>
        <p>{prijmeni}</p>
        <p>{osobni_cislo}</p>
        <p>{cislo_vu}</p>
        <p>{nazev}</p>
      </form>
    </div>
  );
};

export default AddOsoba;
