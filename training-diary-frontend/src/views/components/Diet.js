/* react library imports */
import React, { useState, useEffect } from 'react';

/* Style imports */
import '../../styles/diet.css';

/* React bootstrap imports */
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import Badge from 'react-bootstrap/Badge';
import Button from 'react-bootstrap/Button';
import Tabs from 'react-bootstrap/Tabs';
import Tab from 'react-bootstrap/Tab';


function Diet(props) {

    const[dietEntries, setDietEntries] = useState();

    return (
      <Container>
        <Row>
          <Col xs = {10}>
            <h4> Diet 🍴 </h4>
          </Col>
          <Col xs = {2}>
            <Button className = "add-diet-button" variant = "outline-dark">
              +
            </Button>
          </Col>
        </Row>
        <br/>
        <Row>
            <Col>
              <Tabs defaultActiveKey = "logs">
                <Tab eventKey = "logs" title = "Logs">
                  <br/>
                  <Row>
                    {dietEntries === undefined ?
                      <Col>
                        You have no diet entries...
                      </Col>
                      :
                      <Col>
                        You have diet entries
                      </Col>
                    }
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
            </Col>
        </Row>
      </Container>
    );
}

export default Diet;
