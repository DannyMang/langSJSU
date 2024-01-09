// Chatbox.js
import React, { useState } from 'react';
import './Chatbox.css';
import axios from 'axios';
import Screen from '../Screen/Screen';

function Chatbox() {
  const [showChat, setShowChat] = useState(false);

  const handleEmailSubmit = async(email) => {
      //fix later 
      setShowChat(true);
      try{
        const response = await axios.post(`http://localhost:3500/token?email=${encodeURIComponent(email)}`);
        console.log(response.data);
      }catch (error) {
        console.error('Error fetching token:', error);
      }
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
