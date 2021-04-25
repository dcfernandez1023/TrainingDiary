/* react library imports */
import React, { useState, useEffect } from 'react';

/* React bootstrap imports */
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

/* Controller imports */
const EXERCISE_CONTROLLER = require('../../controllers/exerciseController.js');
const LOCALSTORAGE = require('../../controllers/localStorageHelper.js');


function Exercises(props) {

  const[exercises, setExercises] = useState([]);

  useEffect(() => {
    getExercises();
  }, []);

  const getExercises = () => {
    var token = LOCALSTORAGE.getStorageItem("training-diary-token");
    console.log(token);
    const callback = (res) => {
      console.log(res);
    }
    const callbackOnError = (error) => {
      console.log(error);
    }
    EXERCISE_CONTROLLER.getExercises(props.userInfo.uid, token, callback, callbackOnError);
  }

  return (
    <Container fluid>
      <Row>
        <Col>
        </Col>
      </Row>
    </Container>
  );
}

export default Exercises;
