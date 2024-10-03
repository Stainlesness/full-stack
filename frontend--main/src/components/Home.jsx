import React from 'react';
import { useAuth } from '../auth/AuthProvider';
import { useHistory } from 'react-router-dom';

const Home = () => {
  const { isLoggedIn, role } = useAuth();
  const history = useHistory();

  const goToDashboard = () => {
    switch (role) {
      case 'admin':
        history.push('/admin');
        break;
      case 'bursar':
        history.push('/bursar');
        break;
      case 'director':
        history.push('/director');
        break;
      case 'teacher':
        history.push('/teacher');
        break;
      case 'student':
        history.push('/student');
        break;
      default:
        history.push('/login');
    }
  };

  return (
    <div>
      <h1>Welcome to the School Management System</h1>
      {isLoggedIn ? (
        <button onClick={goToDashboard}>Go to Dashboard</button>
      ) : (
        <button onClick={() => history.push('/login')}>Login</button>
      )}
    </div>
  );
};

export default Home;
