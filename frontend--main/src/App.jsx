import React from 'react';
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import Home from './components/Home';
import LoginForm from './components/LoginForm';
import AdminDashboard from './components/AdminDashboard';
import BursarDashboard from './components/BursarDashboard';
import DirectorDashboard from './components/DirectorDashboard';
import TeacherDashboard from './components/TeacherDashboard';
import StudentDashboard from './components/StudentDashboard';
import { AuthProvider } from './auth/AuthProvider';
import PrivateRoute from './auth/PrivateRoute';
import RoleBasedRoute from './auth/RoleBasedRoute';

const App = () => {
  return (
    <AuthProvider>
      <Router>
        <Switch>
          {/* Public Routes */}
          <Route exact path="/" component={Home} />
          <Route path="/login" component={LoginForm} />

          {/* Private routes for various dashboards */}
          <PrivateRoute path="/admin">
            <RoleBasedRoute role="admin">
              <AdminDashboard />
            </RoleBasedRoute>
          </PrivateRoute>

          <PrivateRoute path="/bursar">
            <RoleBasedRoute role="bursar">
              <BursarDashboard />
            </RoleBasedRoute>
          </PrivateRoute>

          <PrivateRoute path="/director">
            <RoleBasedRoute role="director">
              <DirectorDashboard />
            </RoleBasedRoute>
          </PrivateRoute>

          <PrivateRoute path="/teacher">
            <RoleBasedRoute role="teacher">
              <TeacherDashboard />
            </RoleBasedRoute>
          </PrivateRoute>

          <PrivateRoute path="/student">
            <RoleBasedRoute role="student">
              <StudentDashboard />
            </RoleBasedRoute>
          </PrivateRoute>

          {/* Fallback to Home if route does not match */}
          <Redirect to="/" />
        </Switch>
      </Router>
    </AuthProvider>
  );
};

export default App;
