import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const Kurzy = () => {
  const [kurzy, setKurzy] = useState(null);
  const [isPending, setIsPending] = useState(true);
  const [error, setError] = useState(null);

  const handleDelete = (id) => {
    fetch("/api/kurz/" + id, {
      method: "DELETE",
    }).then((res) => {
      console.log(res);
    });
    const newKurzy = kurzy.filter((kurz) => kurz.id !== id);
    setKurzy(newKurzy);
  };

  useEffect(() => {
    const abortControler = new AbortController();

    setTimeout(() => {
      fetch("/api/kurz/")
        .then((res) => {
          if (!res.ok) {
            throw Error("could not fetch the kurzy for that source");
          }
          return res.json();
        })
        .then((data) => {
          //console.log(data));
          setKurzy(data.data);
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
    <div className="Kurzy">
      <Link
        to="/kurzy/add"
        style={{
          color: "white",
          backgroundColor: "#f1356d",
          borderRadius: "8px",
        }}
      >Přidej kurz
      </Link>
      {error && <div>{error}</div>}
      {isPending && <div>Loading..</div>}
      {kurzy && (
        <div className="blog-list">
          {/* <h2>{title}</h2> */}
          {kurzy.map((kurz) => (
            <div className="blog-preview" key={kurz.id}>
              <Link to={`/utvar/${kurz.id}`}>
                <h2>{kurz.nazev}</h2>
                <h2>{kurz.misto}</h2>
                <h2>{kurz.voj_oznaceni}</h2>
                <h2>{kurz.zacatek_kurzu}</h2>
                <h2>{kurz.konec_kurzu}</h2>
              </Link>
              <button onClick={() => handleDelete(kurz.id)}>
                Delete
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Kurzy;
