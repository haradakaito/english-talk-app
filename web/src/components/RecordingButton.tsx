import React, { useState } from "react";
import "./RecordingButton.css";
import { FaMicrophone } from "react-icons/fa";

const RecordingButton = () => {
const [isRecording, setIsRecording] = useState(false);

const toggleRecording = () => {
    if (isRecording) {
    console.log("🔴 Stop recording");
    } else {
    console.log("🎤 Start recording");
    }
    setIsRecording(!isRecording);
};

return (
    <div className="recording-button-container">
    <button
        className={`record-icon-button ${isRecording ? "active" : ""}`}
        onClick={toggleRecording}
        aria-label="Toggle Recording"
    >
        <FaMicrophone />
    </button>
    </div>
);
};

export default RecordingButton;
