import React from "react";
import Header from "./components/Header.tsx";
import Footer from "./components/Footer.tsx";
import ChatArea from "./components/ChatArea.tsx";
import RecordingButton from "./components/RecordingButton.tsx";
import "./App.css";

function App() {
  return (
    <div className="app-container">
      <Header />
      <div style={{ flex: 1 }}>
        <ChatArea />
      </div>
      <RecordingButton />
      <Footer />
    </div>
  );
}

export default App;