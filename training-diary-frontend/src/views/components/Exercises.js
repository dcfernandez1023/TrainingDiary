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

/* Application imports */
import AddExerciseModal from './AddExerciseModal.js';
import DeleteModal from './DeleteModal.js';
import EditExerciseModal from './EditExerciseModal.js';

/* Controller imports */
const EXERCISE_CONTROLLER = require('../../controllers/exerciseController.js');
const LOCALSTORAGE = require('../../controllers/localStorageHelper.js');


function Exercises(props) {

  const[exercises, setExercises] = useState();
  const[addShow, setAddShow] = useState(false);
  const[deleteShow, setDeleteShow] = useState(false);
  const[editShow, setEditShow] = useState(false);
  const[exerciseToEdit, setExerciseToEdit] = useState();
  const[exerciseToDelete, setExerciseToDelete] = useState();

  useEffect(() => {
    getExercises();
  }, [props.userInfo]);

  const getExercises = () => {
    var token = LOCALSTORAGE.getStorageItem("training-diary-token");
    const callback = (res) => {
      setExercises(res.data.data);
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
    setExerciseToEdit(exercise);
    setEditShow(true);
  }

  const closeEditModal = () => {
    setExerciseToEdit();
    setEditShow(false);
  }

  return (
    <Container fluid>
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
                    onClick = {openAddModal}
                  >
                    +
                  </Button>
                </Col>
              </Row>
            </Card.Header>
            <Card.Body className = "exercise-card-scroll">
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
                          <Col md = {6} key = {index}>
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
                                <Badge pill variant = "light"> {exercise.category} </Badge>
                                <ListGroup variant = "flush">
                                  <ListGroup.Item>
                                     <small> Sets/Reps: </small>
                                     {exercise.sets} x {exercise.reps}
                                   </ListGroup.Item>
                                   <ListGroup.Item>
                                     <small> Amount/Units: </small>
                                     {exercise.amount} {exercise.units}
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
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default Exercises;
