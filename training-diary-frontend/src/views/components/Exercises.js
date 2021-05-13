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
import Spinner from 'react-bootstrap/Spinner';
import ListGroup from 'react-bootstrap/ListGroup';
import Badge from 'react-bootstrap/Badge';
import Tabs from 'react-bootstrap/Tabs';
import Tab from 'react-bootstrap/Tab';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';

/* Application imports */
import AddExerciseModal from './AddExerciseModal.js';
import DeleteModal from './DeleteModal.js';
import EditExerciseModal from './EditExerciseModal.js';
import LogExerciseModal from './LogExerciseModal.js';

/* Controller imports */
const EXERCISE_CONTROLLER = require('../../controllers/exerciseController.js');
const LOCALSTORAGE = require('../../controllers/localStorageHelper.js');


function Exercises(props) {

  const[exercises, setExercises] = useState();
  const[exerciseLog, setExerciseLog] = useState();
  const[exerciseLookup, setExerciseLookup] = useState({});
  const[addShow, setAddShow] = useState(false);
  const[deleteShow, setDeleteShow] = useState(false);
  const[editShow, setEditShow] = useState(false);
  const[logShow, setLogShow] = useState(false);
  const[exerciseToEdit, setExerciseToEdit] = useState();
  const[exerciseToDelete, setExerciseToDelete] = useState();

  useEffect(() => {
    getExercises();
    getExerciseLog();
  }, [props.userInfo]);

  const createExerciseLookup = (exercises) => {
    var lookup = {};
    for(var index in exercises) {
      var exercise = exercises[index];
      lookup[exercise.exercise_id] = exercise;
    }
    setExerciseLookup(lookup);
  }

  const getExercises = () => {
    var token = LOCALSTORAGE.getStorageItem("training-diary-token");
    const callback = (res) => {
      setExercises(res.data.data);
      createExerciseLookup(res.data.data);
    }
    const callbackOnError = (error) => {
      console.log(error);
    }
    if(props.userInfo === undefined || props.userInfo === null) {
      return;
    }
    EXERCISE_CONTROLLER.getExercises(props.userInfo.uid, token, callback, callbackOnError);
  }

  const getExerciseLog = () => {
    var token = LOCALSTORAGE.getStorageItem("training-diary-token");
    const callback = (res) => {
      setExerciseLog(res.data.data);
    }
    const callbackOnError = (error) => {
      console.log(error);
    }
    if(props.userInfo === undefined || props.userInfo === null) {
      return;
    }
    EXERCISE_CONTROLLER.getExerciseLog(props.userInfo.uid, token, callback, callbackOnError);
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

  const logExercises = (logs, modalCallback) => {
    if(props.userInfo === undefined || props.userInfo === null) {
      return;
    }
    if(logs === undefined || logs === null || logs.length === 0) {
      return;
    }
    var token = LOCALSTORAGE.getStorageItem("training-diary-token");
    const callback = (res, loggedExercises) => {
      var ids = res.data.data;
      if(ids.length !== loggedExercises.length) {
        alert("There was an unexpected error in logging your exercises...");
        modalCallback();
        return;
      }
      var exerciseLogCopy = exerciseLog.slice();
      for(var i = 0; i < loggedExercises.length; i++) {
        var log = loggedExercises[i];
        log.exercise_entry_id = ids[i];
        exerciseLogCopy.push(log);
      }
      setExerciseLog(exerciseLogCopy);
      modalCallback();
    }
    const callbackOnError = (error) => {
      console.log(error);
      modalCallback();
    }
    EXERCISE_CONTROLLER.logExercises(props.userInfo.uid, token, logs, callback, callbackOnError);
  }

  const editExercise = (exercise, modalCallback) => {
    if(props.userInfo === undefined || props.userInfo === null) {
      return;
    }
    if(exercise === undefined || exercise === null) {
      return;
    }
    var token = LOCALSTORAGE.getStorageItem("training-diary-token");
    const callback = (res, editedExercise) => {
      var exercisesCopy = exercises.slice();
      for(var i = 0; i < exercisesCopy.length; i++) {
        if(exercisesCopy[i].exercise_id === editedExercise.exercise_id) {
          exercisesCopy[i] = editedExercise;
        }
      }
      setExercises(exercisesCopy);
      modalCallback();
    };
    const callbackOnError = (error) => {
      console.log(error);
      modalCallback();
    }
    EXERCISE_CONTROLLER.editExercise(props.userInfo.uid, token, exercise, callback, callbackOnError);
  }

  const deleteExercise = (modalCallback) => {
    if(props.userInfo === undefined || props.userInfo === null) {
      return;
    }
    if(exerciseToDelete === undefined || exerciseToDelete === null) {
      return;
    }
    var token = LOCALSTORAGE.getStorageItem("training-diary-token");
    const callback = (res, exercise_id) => {
      var exercisesCopy = exercises.slice();
      for(var i = 0; i < exercisesCopy.length; i++) {
        let exercise = exercisesCopy[i];
        if(exercise.exercise_id === exercise_id) {
          exercisesCopy.splice(i, 1);
        }
      }
      setExercises(exercisesCopy);
      closeDeleteModal();
    }
    const callbackOnError = (error) => {
      console.log(error);
      closeDeleteModal();
    }
    EXERCISE_CONTROLLER.deleteExercise(props.userInfo.uid, token, exerciseToDelete, callback, callbackOnError);
  }

  const openAddModal = () => {
    setAddShow(true);
  }

  const closeAddModal = () => {
    setAddShow(false);
  }

  const openDeleteModal = (exercise_id) => {
    setExerciseToDelete(exercise_id);
    setDeleteShow(true);
  }

  const closeDeleteModal = () => {
    setDeleteShow(false);
    setExerciseToDelete();
  }

  const openEditModal = (exercise) => {
    setEditShow(true);
    setExerciseToEdit(exercise);
  }

  const closeEditModal = () => {
    setEditShow(false);
    setExerciseToEdit();
  }

  const openLogModal = () => {
    setLogShow(true);
  }

  const closeLogModal = () => {
    setLogShow(false);
  }

  return (
    <Container>
      <AddExerciseModal
        show = {addShow}
        closeModal = {closeAddModal}
        createExercise = {createExercise}
      />
      <EditExerciseModal
        show = {editShow}
        closeModal = {closeEditModal}
        editExercise = {editExercise}
        exercise = {exerciseToEdit}
      />
      <DeleteModal
        show = {deleteShow}
        closeModal = {closeDeleteModal}
        onClickYes = {deleteExercise}
        onClickNo = {closeDeleteModal}
        header = "Delete Exercise"
        prompt = "Are you sure you want to delete this exercise?"
      />
      <LogExerciseModal
        show = {logShow}
        closeModal = {closeLogModal}
        exercises = {exercises}
        addExercise = {openAddModal}
        logExercises = {logExercises}
        userInfo = {props.userInfo}
      />
      <Row>
        <Col xs = {8}>
          <h4> Exercises 💪 </h4>
        </Col>
        <Col xs = {4}>
          <DropdownButton title = "⚙️" variant = "outline-dark" menuAlign = "right" className = "add-exercise-button" >
            <Dropdown.Item onClick = {() => {openLogModal()}}> Log an Exercise </Dropdown.Item>
            <Dropdown.Item onClick = {() => {openAddModal()}}> Create an Exercise </Dropdown.Item>
          </DropdownButton>
        </Col>
      </Row>
      <br/>
      <Tabs defaultActiveKey = "yourExercises">
        <Tab eventKey = "yourExercises" title = "Your Exercises">
          <br/>
          <Row>
            <Col>
              {exercises === undefined ?
                <div className = "exercise-spinner-align">
                  <Spinner animation = "border" />
                </div>
                :
                <div>
                  {exercises.length === 0 ?
                    <p> You don't have any exercises... </p>
                    :
                    <Row>
                      {exercises.map((exercise, index) => {
                        return (
                          <Col md = {6} lg = {4} sm = {12} key = {index}>
                            <Card className = "exercise-card-spacing">
                              <Card.Header className = "exercise-header-padding">
                                <Row>
                                  <Col xs = {8}>
                                    <p> {exercise.name} </p>
                                  </Col>
                                  <Col xs = {4}>
                                    <Button className = "exercise-btn-option-align" variant = "outline-dark" size = "sm"
                                      onClick = {() => {openDeleteModal(exercise.exercise_id)}}
                                    >
                                      🗑️
                                    </Button>
                                    <Button className = "exercise-btn-option-align" variant = "outline-dark" size = "sm"
                                      onClick = {() => {openEditModal(exercise)}}
                                    >
                                      ✏️
                                    </Button>
                                  </Col>
                                </Row>
                              </Card.Header>
                              <Card.Body className = "exercise-card-body-padding">
                                <Card.Subtitle className = "mb-2 text-muted category-subtitle"> {exercise.category} </Card.Subtitle>
                                {/*<Badge pill variant = "light"> {exercise.category} </Badge>*/}
                                <ListGroup variant = "flush">
                                  <ListGroup.Item>
                                     Sets/Reps - {exercise.sets} x {exercise.reps}
                                   </ListGroup.Item>
                                   <ListGroup.Item>
                                      Amount/Units - {exercise.amount} {exercise.units}
                                   </ListGroup.Item>
                                </ListGroup>
                              </Card.Body>
                            </Card>
                          </Col>
                        );
                      })}
                    </Row>
                  }
                </div>
              }
            </Col>
          </Row>
        </Tab>
        <Tab eventKey = "logs" title = "Logs">
          <br/>
          <Row>
            <Col>
              {exerciseLog === undefined ?
                <div className = "exercise-spinner-align">
                  <Spinner animation = "border" />
                </div>
                :
                <div>
                  {exerciseLog.length === 0 ?
                    <Row>
                      <Col>
                        <h4> You have not logged any exercises </h4>
                      </Col>
                    </Row>
                    :
                    <Row>
                      {exerciseLog.map((log) => {
                        console.log(log);
                        return (
                          <Col md = {12}>
                            <p>
                              {new Date(log.timestamp).toLocaleDateString()} | {log.exercise_entry_id} | {log.exercise_id}
                            </p>
                          </Col>
                        );
                      })}
                    </Row>
                  }
                </div>
              }
            </Col>
          </Row>
        </Tab>
        <Tab eventKey = "insights" title = "Insights">
          <br/>
          <Row>
            <Col>
              Insights coming soon...
            </Col>
          </Row>
        </Tab>
      </Tabs>
    </Container>
  );
}

export default Exercises;
