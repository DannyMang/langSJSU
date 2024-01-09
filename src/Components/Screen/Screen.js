// Screen.js
import React, { useState } from 'react';
import axios from 'axios';
import './Screen.css';

function Screen({ onEmailSubmit }) {
  const [email, setEmail] = useState('');

  const handleSubmit = async () => {
    if ((email.trim() !== '') && email.endsWith('@sjsu.edu')) {
      onEmailSubmit(email)
    } else {
      alert('Please enter a valid SJSU email.');
    }
  };
  

  return (
    <div className="screen-container">
      <h2>Welcome to langSJSU!</h2>
      <p>Please enter your SJSU email to get started:</p>
      <input
        type="email"
        placeholder="Enter your SJSU email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <button onClick={handleSubmit}>Start</button>
    </div>
  );
}

export default Screen;
