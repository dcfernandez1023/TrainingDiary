/* react library imports */
import React, { useState, useEffect } from 'react';

/* Style imports */
//import 'react-calendar/dist/Calendar.css';
import '../../styles/activity.css';

/* React bootstrap imports */
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import Badge from 'react-bootstrap/Badge';
import Button from 'react-bootstrap/Button';

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
      <Calendar
        onChange = {setSelectedDate}
        value = {selectedDate}
        view = "month"
        showNeighboringMonth = {false}
      />
    </Container>
  );
}

export default Activity;
