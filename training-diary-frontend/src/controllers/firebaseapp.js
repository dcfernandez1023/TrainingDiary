var firebase = require('firebase');

const firebaseConfig = {
  apiKey: "AIzaSyB2d4Ucn1ItRysG-RN3ehL3n8KuNOcD60o",
  authDomain: "trainingdiary-5796f.firebaseapp.com",
  projectId: "trainingdiary-5796f",
  storageBucket: "trainingdiary-5796f.appspot.com",
  messagingSenderId: "697417974030",
  appId: "1:697417974030:web:78f23ebd2804d69512d75f",
  measurementId: "G-J6GEWR4DTX"
};

export var app = firebase.default.initializeApp(firebaseConfig);
