import axios from 'axios';

const BASE_URL = "http://localhost:5000";

export const getExercises = (user_id, token, callback, callbackOnError) => {
  var config = {
    headers: {"user_id": user_id, token: token}
  };
  axios.get(BASE_URL + "/api/exercise/getExercises", config)
    .then((res) => {
      callback(res);
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
  console.log(user_id);
  console.log(token);
  console.log(exercise);
  exercise.user_id = user_id;
  axios.post(BASE_URL + "/api/exercise/postExercise", body, config)
    .then((res) => {
      callback(res, exercise);
    }, (error) => {
      callbackOnError(error);
    });
}
