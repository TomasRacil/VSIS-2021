import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="navbar">
      <h1>Template for Frontend</h1>
      <div className="links">
        <Link to="/"
        style={{
          color: "white",
          backgroundColor: "#f1356d",
          borderRadius: "8px",
        }}
        >Home</Link>
        <Link
          to="/register"
          style={{
            color: "white",
            backgroundColor: "#f1356d",
            borderRadius: "8px",
          }}
        >
        New User</Link>
        <Link to="/utvary"
        style={{
          color: "white",
          backgroundColor: "#f1356d",
          borderRadius: "8px",
        }}
        >Utvary</Link>
        <Link to="/osoby"
        style={{
          color: "white",
          backgroundColor: "#f1356d",
          borderRadius: "8px",
        }}
        >Osoby</Link>
        <Link to="/hodnosti"
        style={{
          color: "white",
          backgroundColor: "#f1356d",
          borderRadius: "8px",
        }}
        >Hodnosti</Link>
      </div>
    </nav>
  );
};

export default Navbar;
