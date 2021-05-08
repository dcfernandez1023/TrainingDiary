import axios from 'axios';

const LOCALSTORAGE = require('./localStorageHelper.js');
const BASE_URL = "http://localhost:5000";

export const getExercises = (user_id, token, callback, callbackOnError) => {
  var config = {
    headers: {"user_id": user_id, token: token}
  };
  axios.get(BASE_URL + "/api/exercise/getExercises", config)
    .then((res) => {
      callback(res);
      LOCALSTORAGE.setStorageItem("training-diary-token", res.headers.token);
    }, (error) => {
      callbackOnError(error);
    }
  );
}

export const getExerciseLog = (user_id, token, callback, callbackOnError) => {
  var config = {
    headers: {"user_id": user_id, token: token}
  };
  axios.get(BASE_URL + "/api/exercise/getEntries", config)
    .then((res) => {
      callback(res);
      LOCALSTORAGE.setStorageItem("training-diary-token", res.headers.token);
    }, (error) => {
      callbackOnError(error);
    }
  );
}

export const createExercise = (user_id, token, exercise, callback, callbackOnError) => {
  var config = {
    headers: {"user_id": user_id, token: token}
  };
  var body = {
    data: exercise
  };
  exercise.user_id = user_id;
  axios.post(BASE_URL + "/api/exercise/postExercise", body, config)
    .then((res) => {
      callback(res, exercise);
      LOCALSTORAGE.setStorageItem("training-diary-token", res.headers.token);
    }, (error) => {
      callbackOnError(error);
    });
}

export const logExercises = (user_id, token, logs, callback, callbackOnError) => {
  var config = {
    headers: {"user_id": user_id, token: token}
  };
  var body = {
    data: logs
  };
  axios.post(BASE_URL + "/api/exercise/postEntries", body, config)
    .then((res) => {
      callback(res, logs);
      LOCALSTORAGE.setStorageItem("training-diary-token", res.headers.token);
    }, (error) => {
      callbackOnError(error);
    });
}

export const deleteExercise = (user_id, token, exercise_id, callback, callbackOnError) => {
  var config = {
    headers: {"user_id": user_id, token: token}
  };
  axios.delete(BASE_URL + "/api/exercise/deleteExercise/" + exercise_id, config)
    .then((res) => {
      callback(res, exercise_id);
      LOCALSTORAGE.setStorageItem("training-diary-token", res.headers.token);
    }, (error) => {
      callbackOnError(error);
    });
}

export const editExercise = (user_id, token, exercise, callback, callbackOnError) => {
  var config = {
    headers: {"user_id": user_id, token: token}
  };
  var body = {
    data: exercise
  };
  axios.put(BASE_URL + "/api/exercise/putExercise", body, config)
    .then((res) => {
      callback(res, exercise);
      LOCALSTORAGE.setStorageItem("training-diary-token", res.headers.token);
    }, (error) => {
      callbackOnError(error);
    });
}
