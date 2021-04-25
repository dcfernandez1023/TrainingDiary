/* react library imports */
import React, { useState, useEffect } from 'react';

/* style imports */
import '../../styles/login.css';

/* React bootstrap imports */
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import Tabs from 'react-bootstrap/Tabs';
import Tab from 'react-bootstrap/Tab';
import Image from 'react-bootstrap/Image';

/* Misc */
import GoogleButton from 'react-google-button';

/* Controller imports */
const AUTH = require('../../controllers/auth.js');

function Login(props) {

  const[loginEmail, setLoginEmail] = useState("");
  const[loginPassword, setPassword] = useState("");
  const[registrationEmail, setRegistrationEmail] = useState("");
  const[registrationPassword, setRegistrationPassword] = useState("");
  const[registrationName, setRegistrationName] = useState("");

  const login = () => {
    if(loginEmail.trim().length === 0 || loginPassword.trim().length === 0) {
      return;
    }
    AUTH.standardLogin(loginEmail, loginPassword);
  }

  const register = () => {
    if(registrationEmail.trim().length === 0 || registrationPassword.trim().length === 0) {
      return;
    }
    AUTH.standardRegister(registrationEmail, registrationPassword);
  }

  return (
    <Container>
      <Row className = "top-spacing">
      </Row>
			<Row>
        <Col></Col>
				<Col>
					<Card>
						<Card.Title className = "training-diary-title">
              TrainingDiary
              <Image src = "dumbbell.png" className = "dumbbell-logo"/>
						</Card.Title>
						<Card.Body>
              <Tabs defaultActiveKey = "login" id = "login-register">
                <Tab eventKey = "login" title = "Login">
                  <br/>
                  <div>
                    <Row className = "input-spacing">
                      <Col>
                        <Form.Label> <strong> Email </strong> </Form.Label>
                        <Form.Control
                          as = "input"
                          name = "loginEmail"
                          value = {loginEmail}
                          onChange = {(e) => {
                            setLoginEmail(e.target.value);
                          }}
                        />
                      </Col>
                    </Row>
                    <Row>
                      <Col>
                        <Form.Label> <strong> Password </strong> </Form.Label>
                        <Form.Control
                          type = "password"
                          name = "loginPassword"
                          value = {loginPassword}
                          onChange = {(e) => {
                            setPassword(e.target.value);
                          }}
                        />
                      </Col>
                    </Row>
                    <br/>
                    <Row>
                      <Col>
                        <Button variant = "secondary" onClick = {() => {login()}}> Login </Button>
                      </Col>
                    </Row>
                  </div>
                </Tab>
                <Tab eventKey = "register" title = "Register">
                  <br/>
                  <div>
                  <Row className = "input-spacing">
                    <Col>
                      <Form.Label> <strong> Name </strong> </Form.Label>
                        <Form.Control
                          type = "input"
                          name = "registrationName"
                          value = {registrationName}
                          onChange = {(e) => {
                            setRegistrationName(e.target.value);
                          }}
                        />
                    </Col>
                    </Row>
                    <Row className = "input-spacing">
                      <Col>
                        <Form.Label> <strong> Email </strong> </Form.Label>
                        <Form.Control
                          as = "input"
                          name = "registrationEmail"
                          value = {registrationEmail}
                          onChange = {(e) => {
                            setRegistrationEmail(e.target.value);
                          }}
                        />
                      </Col>
                    </Row>
                    <Row>
                      <Col>
                        <Form.Label> <strong> Password </strong> </Form.Label>
                        <Form.Control
                          type = "password"
                          name = "registrationPassword"
                          value = {registrationPassword}
                          onChange = {(e) => {
                            setRegistrationPassword(e.target.value);
                          }}
                        />
                      </Col>
                    </Row>
                    <br/>
                    <Row>
                      <Col>
                        <Button variant = "secondary" onClick = {() => {register()}}> Register </Button>
                      </Col>
                    </Row>
                  </div>
                </Tab>
              </Tabs>
							<br/>
							<h5> Or </h5>
							<br/>
							<Row>
								<Col>
									<GoogleButton
										type = "light"
                    onClick = {AUTH.googleSignin}
									/>
								</Col>
							</Row>
						</Card.Body>
					</Card>
				</Col>
				<Col></Col>
			</Row>
		</Container>
  );
}

export default Login;
