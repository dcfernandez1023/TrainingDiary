import firebase from 'firebase';
import axios from 'axios';

const firebaseApp = require('./firebaseapp.js');
const AUTH = firebaseApp.app.auth();
const BASE_URL = "http://localhost:5000";
const LOCALSTORAGE = require('./localStorageHelper.js');
const TRAINING_DIARY_TOKEN_KEY = "training-diary-token";

// gets API token from back-end
export const getApiToken = (user_id, callback) => {
	axios.get(BASE_URL + "/api/auth/getApiToken", {headers: {"user_id": user_id}})
		.then((res) => {
			// on success this should return an api token
			LOCALSTORAGE.setStorageItem(TRAINING_DIARY_TOKEN_KEY, res.data.token);
			console.log(res);
		}, (error) => {
			console.log(error);
		});
}

//google authentication method
export const googleSignin = () => {
	var provider = new firebase.auth.GoogleAuthProvider();
	AUTH.signInWithPopup(provider).then(function(result) {
		if(result.additionalUserInfo.isNewUser) {
			let userInfo = result.user;
			axios.post(BASE_URL + "/api/user/postUser", {
					"data": {
						"user_id": userInfo.uid,
						"email": userInfo.email,
						"name": userInfo.displayName
					}
			}).then((res) => {
				console.log(res);
			}, (error) => {
				console.log(error);
			})
		}
	}).catch(function(error) {
		console.log(error);
	});
}

export const standardRegister = (email, password) => {
	AUTH.createUserWithEmailAndPassword(email, password)
		.then((user) => {
			return;
		}).catch((error) => {
			alert(error.message);
		});
}

export const standardLogin = (email, password) => {
	AUTH.signInWithEmailAndPassword(email, password)
		.then((user) => {
			return;
		}).catch((error) => {
			alert(error.message);
		});
}

//signs the user out
export const signout = () => {
	AUTH.signOut().then(function(result) {
		window.location.pathname = "/";
		LOCALSTORAGE.setStorageItem(TRAINING_DIARY_TOKEN_KEY, "");
	}).catch(function(error) {
		alert(error.message);
	});
}

//takes in a callback to capture value from the async callback method passed to onAuthStateChanged
export const isUserSignedin = (userCallback) => {
	AUTH.onAuthStateChanged(function(user) {
		userCallback(user);
		if(user != null) {
			getApiToken(user.uid);
		}
	});
}
