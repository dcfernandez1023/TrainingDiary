/* react library imports */
import React, { useState, useEffect } from 'react';

/* React bootstrap imports */
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Navbar from 'react-bootstrap/Navbar';

/* Application imports */
import Exercises from '../components/Exercises.js';


function Home(props) {

  return (
    <Container fluid>
      <Row>
        <Col>
          <Navbar bg = "light">
            <Navbar.Brand href = "/"> TrainingDiary </Navbar.Brand>
          </Navbar>
        </Col>
      </Row>
      <br/>
      <Row>
        <Col md = {7}>

        </Col>
        <Col md = {5}>
          <Exercises
            userInfo = {props.userInfo}
          />
        </Col>
      </Row>
    </Container>
  );
}

export default Home;
