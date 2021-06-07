import { Link } from "react-router-dom";

const UserList = ({ users, title, handleDelete }) => {
  // const blogs = props.blogs;
  // const title = props.title;
  // console.log(blogs);

  return (
    <div className="blog-list">
      <h2>{title}</h2>
      {users.map((user) => (
        <div className="blog-preview" key={user.public_id}>
          <Link to={`/users/${user.public_id}`}>
            <h2>{user.email}</h2>
            {/* <p>Written by {user.username}</p> */}
          </Link>
          <button onClick={() => handleDelete(user.public_id)}>Delete</button>
        </div>
      ))}
    </div>
  );
};

export default UserList;
