/* react library imports */
import React, { useState, useEffect } from 'react';

/* style imports */
import '../../styles/exercises.css';

/* React bootstrap imports */
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Form from 'react-bootstrap/Form';
import ListGroup from 'react-bootstrap/ListGroup';


function LogExerciseModal(props) {

  const[show, setShow] = useState(false);
  const[logMap, setLogMap] = useState({});

  useEffect(() => {
    setShow(props.show);
  }, [props.show]);

  const handleClose = () => {
    props.closeModal();
    setLogMap({});
  }

  const updateLogMap = (exercise_id) => {
    var logMapCopy = Object.assign({}, logMap);
    if(logMapCopy[exercise_id] !== undefined) {
      delete logMapCopy[exercise_id];
    }
    else {
      logMapCopy[exercise_id] = true;
    }
    setLogMap(logMapCopy);
  }

  return (
    <Modal show = {show} onHide = {handleClose} backdrop = "static">
      <Modal.Header closeButton>
        <Modal.Title> Log Exercise </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        {props.exercises === undefined ?
          <p> An unexpected error occurred. Could not load your exercises. </p>
          :
          <div>
            {props.exercises.length === 0 ?
              <Row>
                <Col>
                  <p> You have no existing exercises to log </p>
                </Col>
              </Row>
              :
              <div>
                <Row>
                  <Col className = "existing-or-create">
                    <p> Choose Existing OR
                      <Button onClick = {props.addExercise} variant = "info" size = "sm" className = "create-new-button">
                        Create New
                      </Button>
                    </p>
                  </Col>
                </Row>
                <br/>
                <Row>
                  <Col>
                    <ListGroup>
                      {props.exercises.map((exercise) => {
                        return (
                            <ListGroup.Item
                              variant = {logMap[exercise.exercise_id] ? "info" : ""}
                              action
                              onClick = {() => {updateLogMap(exercise.exercise_id)}}
                            >
                              {exercise.name} | {exercise.category} | {exercise.sets} x {exercise.reps} of {exercise.amount} {exercise.units}
                            </ListGroup.Item>
                        );
                      })}
                    </ListGroup>
                  </Col>
                </Row>
              </div>
            }
          </div>
        }
      </Modal.Body>
      <Modal.Footer>
        <Button variant = "secondary" onClick = {handleClose}>
          Close
        </Button>
        <Button variant = "success" disabled = {Object.keys(logMap).length === 0}>
          Log Exercises
        </Button>
      </Modal.Footer>
    </Modal>
  );
}

export default LogExerciseModal;
