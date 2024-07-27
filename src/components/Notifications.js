import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Notifications() {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    axios.get('/notifications')
      .then(response => setNotifications(response.data))
      .catch(error => console.error('Error fetching notifications:', error));
  }, []);

  return (
    <div>
      {notifications.map(notification => (
        <div key={notification.notification_id}>
          <p>Message: {notification.message}</p>
          <p>Sent at: {notification.sent_at}</p>
          <hr />
        </div>
      ))}
    </div>
  );
}

export default Notifications;
