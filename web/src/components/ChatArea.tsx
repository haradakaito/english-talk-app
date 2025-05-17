import React from "react";
import "./ChatArea.css";
import AiIcon from "../assets/app-icon.png";

const ChatArea = () => {
return (
    <div className="chat-area-container">
    <div className="chat-messages">
        {/* ユーザーの発話 */}
        <div className="chat-bubble user">
        <div className="bubble">Hello! How are you?</div>
        </div>

        {/* AIの返答 */}
        <div className="chat-bubble ai">
        <img src={AiIcon} alt="AI" className="chat-icon" />
        <div className="bubble">I'm doing great! Ready to chat?</div>
        </div>
    </div>
    </div>
);
};

export default ChatArea;
