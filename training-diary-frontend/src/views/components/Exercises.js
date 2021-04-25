/* react library imports */
import React, { useState, useEffect } from 'react';

/* style imports */
import '../../styles/exercises.css';

/* React bootstrap imports */
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

/* Application imports */
import AddExerciseModal from './AddExerciseModal.js';

/* Controller imports */
const EXERCISE_CONTROLLER = require('../../controllers/exerciseController.js');
const LOCALSTORAGE = require('../../controllers/localStorageHelper.js');


function Exercises(props) {

  const[exercises, setExercises] = useState([]);
  const[show, setShow] = useState(false);

  useEffect(() => {
    getExercises();
  }, [props.userInfo]);

  const getExercises = () => {
    var token = LOCALSTORAGE.getStorageItem("training-diary-token");
    const callback = (res) => {
      setExercises(res.data.data);
      LOCALSTORAGE.setStorageItem("training-diary-token", res.headers.token);
    }
    const callbackOnError = (error) => {
      console.log(error);
    }
    if(props.userInfo === undefined || props.userInfo === null) {
      return;
    }
    EXERCISE_CONTROLLER.getExercises(props.userInfo.uid, token, callback, callbackOnError);
  }

  const createExercise = (exercise, modalCallback) => {
    if(props.userInfo === undefined || props.userInfo === null) {
      return;
    }
    if(exercise === undefined || exercise === null) {
      return;
    }
    var token = LOCALSTORAGE.getStorageItem("training-diary-token");
    const callback = (res, newExercise) => {
      var newExerciseId = res.data.data;
      newExercise.exerciseId = newExerciseId;
      var exercisesCopy = exercises.slice();
      exercisesCopy.push(newExercise);
      setExercises(exercisesCopy);
      modalCallback();
    }
    const callbackOnError = (error) => {
      console.log(error);
      modalCallback();
    }
    EXERCISE_CONTROLLER.createExercise(props.userInfo.uid, token, exercise, callback, callbackOnError);
  }

  const openModal = () => {
    setShow(true);
  }

  const closeModal = () => {
    setShow(false);
  }

  return (
    <Container fluid>
      <AddExerciseModal
        show = {show}
        closeModal = {closeModal}
        createExercise = {createExercise}
      />
      <Row>
        <Col>
          <Card className = "exercise-card-height">
            <Card.Header as = "h5">
              <Row>
                <Col>
                  Exercises 💪
                </Col>
                <Col>
                  <Button className = "add-exercise-button" size = "sm" variant = "outline-dark"
                    onClick = {openModal}
                  >
                    +
                  </Button>
                </Col>
              </Row>
            </Card.Header>
            <Card.Body>
              {exercises.length === 0 ?
                <p> You don't have any exercises... </p>
                :
                <p> You have exercises </p>
              }
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default Exercises;
