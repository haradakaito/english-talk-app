import React, { useState, useRef } from "react";
import "./RecordingButton.css";
import { FaMicrophone } from "react-icons/fa";

const RecordingButton = () => {
const [isRecording, setIsRecording] = useState(false);
const mediaRecorderRef = useRef<MediaRecorder | null>(null);
const chunksRef = useRef<Blob[]>([]);
const timeoutRef = useRef<NodeJS.Timeout | null>(null);

const toggleRecording = async () => {
    if (isRecording) {
    stopRecording();
    } else {
    await startRecording();
    }
};

const startRecording = async () => {
    try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mediaRecorder = new MediaRecorder(stream);

    chunksRef.current = [];

    mediaRecorder.ondataavailable = (e) => {
        if (e.data.size > 0) chunksRef.current.push(e.data);
    };

    mediaRecorder.onstop = () => {
        const audioBlob = new Blob(chunksRef.current, { type: "audio/webm" });

        const url = URL.createObjectURL(audioBlob);
        const audio = new Audio(url);
        audio.play();
    };

    mediaRecorder.start();
    mediaRecorderRef.current = mediaRecorder;
    setIsRecording(true);

    timeoutRef.current = setTimeout(() => {
        stopRecording();
    }, 10000);
    } catch (err) {
        console.error("Error accessing microphone: ", err);
    }
};

const stopRecording = () => {
    if (mediaRecorderRef.current && mediaRecorderRef.current.state !== "inactive") {
    mediaRecorderRef.current.stop();
    }
    setIsRecording(false);
    if (timeoutRef.current) {
    clearTimeout(timeoutRef.current);
    }
};

return (
    <div className="recording-button-container">
    <button
        className={`record-icon-button ${isRecording ? "active" : ""}`}
        onClick={toggleRecording}
        aria-label="Toggle Recording"
    >
        <FaMicrophone size={36} />
    </button>
    </div>
);
};

export default RecordingButton;
