import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AdminDashboard = () => {
  const [students, setStudents] = useState([]);
  const [staff, setStaff] = useState([]);
  const [gallery, setGallery] = useState([]);
  const [notifications, setNotifications] = useState([]);
  const [events, setEvents] = useState([]);

  // Fetch all data on component mount
  useEffect(() => {
    const fetchData = async () => {
      try {
        const studentsResponse = await axios.get('/api/users?role=Student');
        const staffResponse = await axios.get('/api/users?role=Staff');
        const galleryResponse = await axios.get('/api/gallery');
        const notificationsResponse = await axios.get('/api/notifications');
        const eventsResponse = await axios.get('/api/events');

        setStudents(studentsResponse.data);
        setStaff(staffResponse.data);
        setGallery(galleryResponse.data);
        setNotifications(notificationsResponse.data);
        setEvents(eventsResponse.data);
      } catch (err) {
        console.error('Error fetching data', err);
      }
    };
    fetchData();
  }, []);

  // Add a student
  const addStudent = async (studentData) => {
    try {
      await axios.post('/api/users', studentData);
      alert('Student added successfully');
    } catch (err) {
      console.error('Error adding student', err);
    }
  };

  // Add to gallery
  const addGalleryImage = async (imageData) => {
    try {
      await axios.post('/api/gallery', imageData);
      alert('Image added to gallery');
    } catch (err) {
      console.error('Error adding gallery image', err);
    }
  };

  // Add event
  const addEvent = async (eventData) => {
    try {
      await axios.post('/api/events', eventData);
      alert('Event added successfully');
    } catch (err) {
      console.error('Error adding event', err);
    }
  };

  // Add notification
  const addNotification = async (notificationData) => {
    try {
      await axios.post('/api/notifications', notificationData);
      alert('Notification added successfully');
    } catch (err) {
      console.error('Error adding notification', err);
    }
  };

  return (
    <div>
      <h2>Admin Dashboard</h2>

      {/* Section for adding students */}
      <h3>Add a Student</h3>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          addStudent({
            name: e.target.name.value,
            admission_number: e.target.admission_number.value,
            grade: e.target.grade.value,
            role: 'Student',
          });
        }}
      >
        <input name="name" placeholder="Student Name" required />
        <input name="admission_number" placeholder="Admission Number" required />
        <input name="grade" placeholder="Grade" required />
        <button type="submit">Add Student</button>
      </form>

      {/* Section for viewing students and their balances */}
      <h3>Student List and Balances</h3>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Admission Number</th>
            <th>Grade</th>
            <th>Balance</th>
          </tr>
        </thead>
        <tbody>
          {students.map((student) => (
            <tr key={student.id}>
              <td>{student.name}</td>
              <td>{student.admission_number}</td>
              <td>{student.grade}</td>
              <td>{student.balance}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Section for gallery */}
      <h3>Gallery</h3>
      <ul>
        {gallery.map((image) => (
          <li key={image.id}>
            {image.name} - {image.description}
          </li>
        ))}
      </ul>
      <h4>Add to Gallery</h4>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          addGalleryImage({
            name: e.target.name.value,
            description: e.target.description.value,
            file: e.target.file.files[0], // Assuming file upload
          });
        }}
      >
        <input name="name" placeholder="Image Name" required />
        <input name="description" placeholder="Image Description" required />
        <input type="file" name="file" required />
        <button type="submit">Add Image</button>
      </form>

      {/* Section for staff management */}
      <h3>Staff List</h3>
      <ul>
        {staff.map((person) => (
          <li key={person.id}>
            {person.name} - {person.role}
          </li>
        ))}
      </ul>

      {/* Section for events */}
      <h3>Upcoming Events</h3>
      <ul>
        {events.map((event) => (
          <li key={event.id}>
            {event.title} - {event.date} - {event.destination}
          </li>
        ))}
      </ul>
      <h4>Add Event</h4>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          addEvent({
            title: e.target.title.value,
            date: e.target.date.value,
            destination: e.target.destination.value,
            description: e.target.description.value,
          });
        }}
      >
        <input name="title" placeholder="Event Title" required />
        <input name="date" type="date" required />
        <input name="destination" placeholder="Event Destination" required />
        <textarea name="description" placeholder="Event Description" required></textarea>
        <button type="submit">Add Event</button>
      </form>

      {/* Section for notifications */}
      <h3>Notifications</h3>
      <ul>
        {notifications.map((notification) => (
          <li key={notification.id}>{notification.message}</li>
        ))}
      </ul>
      <h4>Add Notification</h4>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          addNotification({
            message: e.target.message.value,
          });
        }}
      >
        <textarea name="message" placeholder="Notification Message" required></textarea>
        <button type="submit">Add Notification</button>
      </form>
    </div>
  );
};

export default AdminDashboard;
