// Chatbox.js
import React, { useState } from 'react';
import './Chatbox.css';
import Screen from '../Screen/Screen';

function Chatbox() {
  const [showChat, setShowChat] = useState(false);

  const handleEmailSubmit = (email) => {
      //TO - DO 
    setShowChat(true);
  };

  return (
    <div className="chatbox-container">
      {!showChat ? (
        <Screen onEmailSubmit={handleEmailSubmit} />
      ) : (
        <>
          <div className="chatbox-messages">
            {/* Messages will be displayed here */}
          </div>
          <div className="user-input">
            <input type="text" placeholder="Type your message..." />
            <button>Send</button>
          </div>
        </>
      )}
    </div>
  );
}

export default Chatbox;
