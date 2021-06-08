import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const Hodnosti = () => {
  const [hodnosti, setHodnosti] = useState(null);
  const [isPending, setIsPending] = useState(true);
  const [error, setError] = useState(null);

  const handleDelete = (id) => {
    fetch("/api/hodnost/" + id, {
      method: "DELETE",
    }).then((res) => {
      console.log(res);
    });
    const newHodnosti = hodnosti.filter((hodnost) => hodnost.id !== id);
    setHodnosti(newHodnosti);
  };

  useEffect(() => {
    const abortControler = new AbortController();

    setTimeout(() => {
      fetch("/api/hodnost/")
        .then((res) => {
          if (!res.ok) {
            throw Error("could not fetch the data for that source");
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
    }, 1000);

    return () => abortControler.abort();
  }, []);

  return (
    <div className="Hodnosti">
      <Link
        to="/hodnosti/add"
        style={{
          backgroundColor: "rgb(241, 53, 109)",
          color: "white",
          borderRadius: "8px",
        }}
      >Přidej hodnost
      </Link>
      {error && <div>{error}</div>}
      {isPending && <div>Loading..</div>}
      {hodnosti && (
        <div className="blog-list">
          {/* <h2>{title}</h2> */}
          {hodnosti.map((hodnost) => (
            <div className="blog-preview" key={hodnost.id}>
              <Link to={`/hodnost/${hodnost.id}`}>
                <h2>{hodnost.nazev}</h2>
                <h2>{hodnost.hodnostni_sbor}</h2>
              </Link>
              {<button onClick={() => handleDelete(hodnost.id)}>
                Delete
              </button>}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Hodnosti;
