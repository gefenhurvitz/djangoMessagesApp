import React, { useState } from "react";
import { useParams } from "react-router-dom";

const NotePage = (props) => {
  // get the id param from the url
  let { id } = useParams();

  //   set the useState for the note
  const [note, setNote] = useState(null);

  // set the function that set the note state using the id fro the url
  // const getNote =  async () => {
  //     const res = fetch(`http://127.0.0.1:8000/notes/${id}`)
  //     const data = await res.json();
  //     console.log(data);
  //     setNote(data);
  // }

  return (
    <div>
      {/* <button onClick={()=>{getNote()}}>get note</button> */}
      {/* <h1>{note.body}</h1> */}

      <h1>single page {id}</h1>
    </div>
  );
};

export default NotePage;
