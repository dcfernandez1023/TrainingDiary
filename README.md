# TrainingDiary

## Description
This is a web application that allows users to digitally journal and view their workout data. The main goal of this application is to provide what I like to call "instinctive trainers" with a way to track, view, and analyze their workout data.

Many avid gym-goers don't always follow a set-in-stone workout plan, where they plan a 6 month exercise schedule and adhere to it. Though some may follow a structured workout plan, many people like to go the gym and sort of dynamically plan their workout based on what they feel like doing that day. However, due to this dynamic planning, it makes it more difficult to track the workouts that they do and visualize any progress that they make unless they do it manually in a notebook or type it out on an editor afterwards, which is tedious and leaves out the potential for the analysis and visualization of their data.   

And that is the problem that this application works to solve - to make it less mechanical for these "instinctive trainers" (like myself) to document their workouts and progress.  

## Project Structure
The main directories and files of this application:

    training-diary-backend/
         controllers
         db
         models
         routes
         tests
         utilities
         routes
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
- React/Node.js
- HTML/CSS
- React Bootstrap
- Firebase (deployment + user-authentication)

### Back-end
- Python
- Flask
- JWT (token-based authentication for endpoints)
- Gunicorn
- PostgreSQL
- Heroku (deployment)
