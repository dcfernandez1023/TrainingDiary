# TrainingDiary

A web application that allows you to track, analyze, and receive insights on your workout data.

## Project Structure
The main directories and files of this application:

    training-diary-backend/
         blueprints
         controllers
         db
         models
         tests
         app.py
     training-diary-frontend/
        public
        src/
            controllers
            models
            styles
            views
            index.js

### Front-end
Technologies Used:
- React/Node.js
- HTML/CSS
- React Bootstrap

`training-diary-frontend` contains all the files for the React/Node.js frontend to operate. The `public` directory contains the entry point to the single-page application, `index.html`, and other resources that should be available publicly to users of the front-end. The `src` directory contains all of the logic for the front-end, including its `controllers` (provides layer of access to back-end), `models` (front-end objects/metadata shared across components), `styles` (CSS files), `views` (components for rendering various aspects of the front-end), and `index.js` (packages it all together into one .js file).

### Back-end
Technologies Used:
- Flask
- Sqlite3

`training-diary-backend` contains all the files for the python backend to operate. The `blueprints` directory contains the endpoints that the Flask app will expose as well as the logic behind each endpoint. 
