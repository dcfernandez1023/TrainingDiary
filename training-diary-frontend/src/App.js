/* react library imports */
import React, { useState, useEffect } from 'react';

/* style imports */
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/App.css';
import './styles/login.css';

/* React bootstrap imports */
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

/* Application imports */
import Login from './views/pages/Login.js';
import Home from './views/pages/Home.js';

/* External library imports */
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

/* Controller imports */
const AUTH = require('./controllers/auth.js');


function App() {

  const[userInfo, setUserInfo] = useState();

  useEffect(() => {
    isUserSignedin();
  }, []);

  //sets userInfo state object
  //passes a call back to AUTH controller to set state object of this component
  const isUserSignedin = () => {
    const callback = (user) => {
      setUserInfo(user);
    }
    AUTH.isUserSignedin(callback);
  }

  return (
    <Router>
      <Switch>
        <Route exact path = "/">
          {userInfo === null ?
            <body className = "login-background">
              <Login/>
            </body>
          :
          <body className = "home-background-color home-overflow">
            <Home
              userInfo = {userInfo}
            />
          </body>
          }
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
