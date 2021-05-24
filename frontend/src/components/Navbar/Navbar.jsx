import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="navbar">
      <h1>Template for Frontend</h1>
      <div className="links">
        <Link to="/">Home</Link>
        <Link
          to="/register"
          style={{
            color: "white",
            backgroundColor: "#f1356d",
            borderRadius: "8px",
          }}
        >
          New User
        </Link>
        <Link to="/utvary">Utvary</Link>
      </div>
    </nav>
  );
};

export default Navbar;
