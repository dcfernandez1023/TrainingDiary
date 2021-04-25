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

/* Model imports */
const EXERCISE_MODEL = require('../../models/exercise.js');


function AddExerciseModal(props) {

  const[newExercise, setNewExercise] = useState({});
  const[show, setShow] = useState(false);

  useEffect(() => {
    if(Object.keys(newExercise).length === 0) {
      setNewExercise(Object.assign({}, EXERCISE_MODEL.exercise));
    }
    setShow(props.show);
  }, [props.show]);

  const handleClose = () => {
    props.closeModal();
    setNewExercise({});
  }

  const onChangeExercise = (e) => {
    var name = e.target.name;
    var value = e.target.value;
    if(EXERCISE_MODEL.exerciseMetaData[name].type === "number" && isNaN(value)) {
      return;
    }
    var newExerciseCopy = Object.assign({}, newExercise);
    newExerciseCopy[name] = value;
    setNewExercise(newExerciseCopy);
  }

  const onClickCreate = () => {
    var newExerciseCopy = Object.assign({}, newExercise);
    for(var i = 0; i < EXERCISE_MODEL.exerciseFields.length; i++) {
      let field = EXERCISE_MODEL.exerciseFields[i];
      let metaData = EXERCISE_MODEL.exerciseMetaData[field];
      if(metaData.editable && newExerciseCopy[field].trim().length === 0) {
        alert("You are missing required fields");
        return;
      }
      if(typeof(newExerciseCopy[field]) === "number") {
        newExerciseCopy[field] = parseInt(newExerciseCopy[field]);
      }
    }
    props.createExercise(newExerciseCopy, props.closeModal);

  }

  return (
    <Modal show = {show} onHide = {handleClose} backdrop = "static">
      <Modal.Header closeButton>
        <Modal.Title> Create Exercise </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Row>
          {EXERCISE_MODEL.exerciseFields.map((field, index) => {
            var metaData = EXERCISE_MODEL.exerciseMetaData[field];
            if(metaData.elementType === "input") {
              return (
                <Col md = {12}>
                  <Form.Label> {metaData.displayName} </Form.Label>
                  <Form.Control
                    key = {field + index.toString()}
                    as = {metaData.elementType}
                    name = {field}
                    value = {newExercise[field]}
                    onChange = {(e) => {onChangeExercise(e)}}
                    className = "modal-input-spacing"
                  />
                </Col>
              );
            }
            else if(metaData.elementType === "select") {
              return (
                <Col md = {12}>
                  <Form.Label> {metaData.displayName} </Form.Label>
                  <Form.Control
                    key = {field + index.toString()}
                    as = {metaData.elementType}
                    type = {metaData.type === "number" ? "number" : "input"}
                    name = {field}
                    value = {newExercise[field]}
                    onChange = {(e) => {onChangeExercise(e)}}
                    className = "modal-input-spacing"
                  >
                    <option value = "none" selected> Select </option>
                    {metaData.options.map((option, index) => {
                      return (
                        <option key = {option + index.toString()} value = {option}> {option} </option>
                      );
                    })}
                  </Form.Control>
                </Col>
              );
            }
          })}
        </Row>
      </Modal.Body>
      <Modal.Footer>
        <Button variant = "secondary"
          onClick = {handleClose}
        >
          Close
        </Button>
        <Button variant = "success"
          onClick = {() => {onClickCreate()}}
        >
          Create
        </Button>
      </Modal.Footer>
    </Modal>
  );
}


export default AddExerciseModal;
