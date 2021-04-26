/* react library imports */
import React, { useState, useEffect } from 'react';

/* React bootstrap imports */
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Spinner from 'react-bootstrap/Spinner';
import Modal from 'react-bootstrap/Modal';


function DeleteModal(props) {

  const[show, setShow] = useState(false);

  useEffect(() => {
    setShow(props.show);
  }, [props.show]);

  return (
    <Modal
      show = {show}
      onHide = {props.closeModal}
      backdrop = "static"
    >
      <Modal.Header closeButton> {props.header} </Modal.Header>
      <Modal.Body>
        <p> {props.prompt} </p>
      </Modal.Body>
      <Modal.Footer>
        <Button variant = "secondary" onClick = {props.onClickNo}>
          No
        </Button>
        <Button variant = "danger" onClick = {props.onClickYes}>
          Yes
        </Button>
      </Modal.Footer>
    </Modal>
  );
}

export default DeleteModal;
