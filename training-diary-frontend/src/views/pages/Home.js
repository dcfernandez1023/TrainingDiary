/* react library imports */
import React, { useState, useEffect } from 'react';

/* Style imports */
import '../../styles/home.css';

/* React bootstrap imports */
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import Button from 'react-bootstrap/Button';
import Dropdown from 'react-bootstrap/Dropdown';
import NavDropdown from 'react-bootstrap/NavDropdown';

/* Application imports */
import Exercises from '../components/Exercises.js';
import Activity from '../components/Activity.js';
import Diet from '../components/Diet.js';

/* Controller imports */
const AUTH = require('../../controllers/auth.js');


function Home(props) {

  const TAB_COMPONENTS = [
    <Activity
      userInfo = {props.userInfo}
    />,
    <Exercises
      userInfo = {props.userInfo}
    />,
    <Diet
      userInfo = {props.userInfo}
    />
  ];

  const[currentTab, setCurrentTab] = useState(0);


  return (
    <Container fluid>
      <Row>
        <Col>
          <Navbar bg = "info" variant = "dark" collapseOnSelect expand = "lg">
            <Navbar.Brand href = "/"> TrainingDiary </Navbar.Brand>
            <Navbar.Toggle aria-controls = "responsive-navbar-nav" />
            <Navbar.Collapse id = "responsive-navbar-nav">
              <Nav defaultActiveKey = {0} className = "option-nav"
                onSelect = {(eventKey) => {setCurrentTab(eventKey)}}
              >
                <Nav.Link eventKey = {0}> Activity </Nav.Link>
                <Nav.Link eventKey = {1}> Exercise </Nav.Link>
                <Nav.Link eventKey = {2}> Diet </Nav.Link>
                <Nav.Link eventKey = {3}> Body </Nav.Link>
                <Nav.Link eventKey = {4}> Custom </Nav.Link>
              </Nav>
              <Nav className="mr-auto">
              </Nav>
              <Nav>
                <Button variant = "outline-dark"> Profile </Button>
              </Nav>
            </Navbar.Collapse>
          </Navbar>
        </Col>
      </Row>
      <br/>
      <Row>
        {TAB_COMPONENTS[currentTab]}
      </Row>
    </Container>
  );
}

export default Home;
