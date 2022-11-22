import "./App.css";
import Header from "./components/Header";
import NotesListPage from "./pages/NotesListPage";

import React from "react";
import { Route, Routes } from "react-router-dom";
import NotePage from "./pages/NotePage";

function App() {
  return (
    <>
      <div className="App">
        <Header />

        <Routes>
          <Route path="/notes" exact element={<NotesListPage />} />
          <Route path="/notes/:id" element={<NotePage />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
