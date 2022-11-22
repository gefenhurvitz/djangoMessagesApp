import React from "react";
import {Link} from 'react-router-dom'

const ListItem = ({ note, index }) => {
  return (
    <Link to={`/notes/${index+1}`}>
      <div>
        <h3>
          {index + 1}: {note.body}
        </h3>
      </div>
    </Link>
  );
  //  to={`/note/${id}`}
};

export default ListItem;
