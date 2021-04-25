import axios from 'axios';

const BASE_URL = "http://localhost:5000";

export const getExercises = (user_id, token, callback, callbackOnError) => {
  axios.get(BASE_URL + "/api/exercise/getExercises", {
    headers: {
      user_id: user_id,
      token: token
    }
  }).then((res) => {
    callback(res);
  }, (error) => {
    callbackOnError(error);
  });
}
