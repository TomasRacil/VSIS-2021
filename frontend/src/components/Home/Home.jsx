import { useEffect, useState } from "react";
import UserList from "../BlogList/UserList";

const Home = () => {
  //   const [blogs, setBlogs] = useState([
  //     { title: "My new website", body: "lorem ipsum...", author: "mario", id: 1 },
  //     { title: "Welcome party!", body: "lorem ipsum...", author: "yoshi", id: 2 },
  //     {
  //       title: "Web dev top tips",
  //       body: "lorem ipsum...",
  //       author: "mario",
  //       id: 3,
  //     },
  //   ]);
  const [users, setUsers] = useState(null);

  //   const [name, setName] = useState("mario");
  const [isPending, setIsPending] = useState(true);
  const [error, setError] = useState(null);

  const handleDelete = (id) => {
    const newUsers = users.filter((user) => user.public_id !== id);
    setUsers(newUsers);
  };

  useEffect(() => {
    setTimeout(() => {
      fetch("/api/user/")
        .then((res) => {
          console.log(res);
          if (!res.ok) {
            throw Error("could not fetch the data for that source");
          }
          return res.json();
        })
        .then((data) => {
          console.log(data.data);
          setUsers(data.data);
          setIsPending(false);
          setError(null);
        })
        .catch((err) => {
          setIsPending(false);
          setError(err.message);
        });
    }, 1000);

    //console.log("use effect ran");
  }, []); //only initial render
  //[name]); //declare watched item

  return (
    <div className="home">
      {error && <div>{error}</div>}
      {isPending && <div>Loading..</div>}
      {users && (
        <UserList users={users} title="All Users" handleDelete={handleDelete} />
      )}
      {/* <BlogList
        blogs={blogs.filter((blog) => blog.author === "mario")}
        title="Mario's Blogs"
      /> */}
      {/* <button onClick={() => setName("luigi")}>Change name</button> */}
      {/* <p>{name}</p> */}
    </div>
  );
};

export default Home;
