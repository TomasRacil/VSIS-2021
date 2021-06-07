import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const Utvary = () => {
  const [utvary, setUtvary] = useState(null);
  const [isPending, setIsPending] = useState(true);
  const [error, setError] = useState(null);

  const handleDelete = (id) => {
    fetch("/api/utvar/" + id, {
      method: "DELETE",
    }).then((res) => {
      console.log(res);
    });
    const newUtvary = utvary.filter((utvar) => utvar.id !== id);
    setUtvary(newUtvary);
  }; 

  useEffect(() => {
    const abortControler = new AbortController();

    setTimeout(() => {
      fetch("/api/utvar/")
        .then((res) => {
          if (!res.ok) {
            throw Error("could not fetch the data for that source");
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
    }, 1000);

    return () => abortControler.abort();
  }, []);

  return (
    <div className="Utvary">
      <Link
          to="/utvary/add"
          style={{
            color: "white",
            backgroundColor: "#f1356d",
            borderRadius: "8px",
          }}
        >Pridej utvar</Link>
      {error && <div>{error}</div>}
      {isPending && <div>Loading..</div>}
      {utvary && (
        <div className="blog-list">
          {/* <h2>{title}</h2> */}
          {utvary.map((utvar) => (
            <div className="blog-preview" key={utvar.cislo_vu}>
              <Link to={`/utvar/${utvar.cislo_vu}`}>
                <h2>{utvar.nazev_utvaru}</h2>
                <p> {utvar.lokace}</p>
                <button onClick={() => handleDelete(utvar.id)}>Delete</button>
              </Link>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Utvary;
