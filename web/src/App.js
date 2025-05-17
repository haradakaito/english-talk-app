import React from "react";
import "./App.css";

function App() {
  return (
    <div className="app-container">

      <div className="chat-box">
        <div className="chat-message user">
          <strong></strong> Hello! How can I help you today?
        </div>
        <div className="chat-message ai">
          <strong></strong> Hi! I need some assistance with my order.
        </div>
      </div>

      <button className="record-button">Start Recording</button>
    </div>
  );
}

export default App;
