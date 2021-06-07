import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const Osoby = () => {
  const [osoby, setOsoby] = useState(null);
  const [isPending, setIsPending] = useState(true);
  const [error, setError] = useState(null);

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
                {/* <h2>{Hodnost.nazev.label("hodnost")}</h2>
                <h2>{Utvar.cislo_vu.label("utvar")}</h2> */}
                {/* <button onClick={() => handleDelete(user.public_id)}>Delete</button> */}
              </Link>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Osoby;
