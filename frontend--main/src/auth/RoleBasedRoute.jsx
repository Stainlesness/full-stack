import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import { useAuth } from './AuthProvider';

const RoleBasedRoute = ({ role, children, ...rest }) => {
  const { role: userRole } = useAuth();

  return (
    <Route
      {...rest}
      render={({ location }) =>
        userRole === role ? (
          children
        ) : (
          <Redirect
            to={{
              pathname: "/",
              state: { from: location }
            }}
          />
        )
      }
    />
  );
};

export default RoleBasedRoute;
