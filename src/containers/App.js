import React from 'react';
import FlightStatus from '../components/FlightStatus';
import Notifications from '../components/Notifications';

function App() {
  return (
    <div className="App">
      <h1>Flight Status</h1>
      <FlightStatus />
      <h2>Notifications</h2>
      <Notifications />
    </div>
  );
}

export default App;
