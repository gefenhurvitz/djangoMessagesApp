import React, { useState } from "react";
import ListItem from "../components/ListItem";

const NotesListPage = () => {
  const [notes, setNotes] = useState([]);

  const getNotes = async () => {
    const res = await fetch("http://127.0.0.1:8000/notes/");
    const data = await res.json();
    console.log(data);
    setNotes(data);
  };

  return (
    <div>
      <h1>hello</h1>
      <button
        onClick={() => {
          getNotes();
        }}
      >
        get data
      </button>
      <hr />

      <h1>{notes.title}</h1>

      <div className="notes-list">
        {notes.map((note, index) => (
          <ListItem key={index} note={note} index={index} />
        ))}
      </div>
    </div>
  );
};

export default NotesListPage;
