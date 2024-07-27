// FlightStatus.js
import React, { useState, useEffect } from 'react';
import { messaging } from '../firebase';
import axios from 'axios';

const FlightStatus = () => {
  const [flightStatus, setFlightStatus] = useState({
    status: 'Unknown',
    gate: '',
    departureTime: '',
  });

  useEffect(() => {
    // Initialize FCM
    messaging.requestPermission().then(() => {
      messaging.getToken().then(token => {
        console.log('Device token:', token);
        // Register device token with your server
      });
    });
  }, []);

  useEffect(() => {
    // Fetch flight data from API
    axios.get('http://127.0.0.1:5000/flights/6E 2341/status')
      .then(response => {
        setFlightStatus(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handleFlightStatusUpdate = (status) => {
    setFlightStatus(status);
  };

  return (
    <div>
      <h1>Flight Status: {flightStatus.status}</h1>
      <p>Gate: {flightStatus.gate}</p>
      <p>Departure Time: {flightStatus.departureTime}</p>
    </div>
  );
};

export default FlightStatus;