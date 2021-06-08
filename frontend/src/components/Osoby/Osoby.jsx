import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const Osoby = () => {
  const [osoby, setOsoby] = useState(null);
  const [isPending, setIsPending] = useState(true);
  const [error, setError] = useState(null);

  const handleDelete = (id) => {
    fetch("/api/osoba/" + id, {
      method: "DELETE",
    }).then((res) => {
      console.log(res);
    });
    const newOsoby = osoby.filter((osoba) => osoba.id !== id);
    setOsoby(newOsoby);
  }; 

  useEffect(() => {
    const abortControler = new AbortController();

    setTimeout(() => {
      fetch("/api/osoba/")
        .then((res) => {
          if (!res.ok) {
            throw Error("could not fetch the data for that source");
          }
          return res.json();
        })
        .then((data) => {
          //console.log(data));
          setOsoby(data.data);
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
    }, 1000);

    return () => abortControler.abort();
  }, []);

  return (
    <div className="Osoby">
      <Link
          to="/osoby/add"
          style={{
            color: "white",
            backgroundColor: "rgb(241, 53, 109)",
            borderRadius: "8px",
          }}
        >Přidej osobu</Link>
      {error && <div>{error}</div>}
      {isPending && <div>Loading..</div>}
      {osoby && (
        <div className="blog-list">
          {/* <h2>{title}</h2> */}
          {osoby.map((osoba) => (
            <div className="blog-preview" key={osoba.id}>
              <Link to={`/osoba/${osoba.id}`}>
                <h2>{osoba.jmeno}</h2>
                <h2>{osoba.prijmeni}</h2>
                <h2>{osoba.osobni_cislo}</h2>
                {<button onClick={() => handleDelete(osoba.id)}>
                  Delete
                  </button>}
              </Link>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Osoby;
