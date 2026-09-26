import { Link, useNavigate } from "react-router-dom";

function Navbar() {
  const token = localStorage.getItem("access_token");
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    navigate("/login");
  };

  return (
    <nav>
      <Link to="/">WowPatterns</Link>{" "}
      <Link to="/">Home</Link>{" "}
      <Link to="/products">Products</Link>{" "}

      {!token && <Link to="/login">Login</Link>}

      {token && (
        <>
          <Link to="/profile">Profile</Link>{" "}
          <button type="button" onClick={handleLogout}>
            Logout
          </button>
        </>
      )}
    </nav>
  );
}

export default Navbar;