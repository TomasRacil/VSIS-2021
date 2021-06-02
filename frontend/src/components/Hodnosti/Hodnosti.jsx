import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const Hodnosti = () => {
  const [hodnosti, setHodnosti] = useState(null);
  const [isPending, setIsPending] = useState(true);
  const [error, setError] = useState(null);

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
      {error && <div>{error}</div>}
      {isPending && <div>Loading..</div>}
      {hodnosti && (
        <div className="blog-list">
          {/* <h2>{title}</h2> */}
          {hodnosti.map((hodnost) => (
            <div className="blog-preview" key={hodnosti.id}>
              <Link to={`/hodnost/${hodnost.id}`}>
                <h2>{hodnost.nazev}</h2>
                <p> {hodnost.hodnostni_sbor}</p>
                {/* <button onClick={() => handleDelete(user.public_id)}>Delete</button> */}
              </Link>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Hodnosti;
