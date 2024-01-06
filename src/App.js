// App.js
import React from 'react';
import './App.css';
import Chatbox from './Components/Chatbox/Chatbox'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div className="logo-container">
          <p className="logo-text">langSJSU</p>
        </div>
      </header>
      <Chatbox />
    </div>
  );
}

export default App;
