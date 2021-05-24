import { useEffect, useState } from "react";
const Utvary = () => {
  const [utvary, setUtvary] = useState(null);
  function get_utvary() {
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
      })
      .catch((err) => {
        if (err.name === "AbortError") {
          console.log("fetch aborted");
        } else {
          //setIsPending(false);
          //setError(err.message);
        }
      });
  }
  return (
    <div className="Utvary">
      <button onClick={get_utvary}>Utvary</button>
      <button onClick={console.log(utvary[0])}>show</button>
      {/* {utvary} */}
    </div>
  );
};

export default Utvary;
