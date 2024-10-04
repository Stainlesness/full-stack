import React from 'react';
import { useAuth } from '../auth/AuthProvider';
import { useNavigate } from 'react-router-dom';

const Home = () => {
  const { isLoggedIn, role } = useAuth();
  const navigate = useNavigate();

  const goToDashboard = () => {
    switch (role) {
      case 'admin':
        navigate('/admin');
        break;
      case 'bursar':
        navigate('/bursar');
        break;
      case 'director':
        navigate('/director');
        break;
      case 'teacher':
        navigate('/teacher');
        break;
      case 'student':
        navigate('/student');
        break;
      default:
        navigate('/login');
    }
  };

  return (
    <div>
      <h1>Welcome to the School Management System</h1>
      {isLoggedIn ? (
        <button onClick={goToDashboard}>Go to Dashboard</button>
      ) : (
        <button onClick={() => navigate('/login')}>Login</button>
      )}
    </div>
  );
};

export default Home;
