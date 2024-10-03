import React, { useState } from 'react';
import { useAuth } from '../auth/AuthProvider';
import { useHistory } from 'react-router-dom';

const LoginForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useAuth();
  const history = useHistory();

  const handleLogin = (e) => {
    e.preventDefault();

    // Call your backend for authentication (mock example)
    const role = username === 'admin' ? 'admin' : 'student'; // Example logic
    login(role);

    history.push('/');
  };

  return (
    <form onSubmit={handleLogin}>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        required
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      <button type="submit">Login</button>
    </form>
  );
};

export default LoginForm;