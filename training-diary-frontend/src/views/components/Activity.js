/* react library imports */
import React, { useState, useEffect } from 'react';

/* Style imports */
import '../../styles/activity.css';

/* React bootstrap imports */
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import Badge from 'react-bootstrap/Badge';
import Button from 'react-bootstrap/Button';
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import Tooltip from 'react-bootstrap/Tooltip';

/* Misc */
import Calendar from 'react-calendar';


function Activity() {

  const[startDate, setStartDate] = useState();
  const[endDate, setEndDate] = useState();
  const[selectedDate, setSelectedDate] = useState(new Date());

  useEffect(() => {
    init_start_date()
    init_end_date();
  }, []);

  const init_start_date = () => {
    var date = new Date();
    var firstDay = new Date(date.getFullYear(), date.getMonth(), 1);
    setStartDate(firstDay);
  }

  const init_end_date = () => {
    var date = new Date();
    var lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);
    setEndDate(lastDay);
  }

  return (
    <Container>
      <Row>
        <Col xs = {10}>
          <h4> Activity 🏃 </h4>
        </Col>
        <Col xs = {2}>
          <Button className = "add-activity-button" variant = "outline-dark"> + </Button>
        </Col>
      </Row>
      <Row>
        <Col>
          <Badge className = "badge-spacing" pill variant = "dark"> 🔥 Activity Streak: 3 </Badge>
          <Badge className = "badge-spacing" pill variant = "dark"> 🏆 Active Days: 3/30 </Badge>
        </Col>
      </Row>
      <br/>
      <Row>
        <Col>
          <Calendar
            onChange = {setSelectedDate}
            value = {selectedDate}
            view = "month"
            showNeighboringMonth = {false}
            tileClassName = "custom-tile"
          />
        </Col>
      </Row>
    </Container>
  );
}

export default Activity;
