// src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [flights, setFlights] = useState([]);

  useEffect(() => {
    axios.get('/api/flights')
      .then(response => setFlights(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="App">
      <h1>Flight Status</h1>
      <ul>
        {flights.map(flight => (
          <li key={flight.id}>
            {flight.number}: {flight.status}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
