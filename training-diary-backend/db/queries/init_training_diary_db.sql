DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Activities;
DROP TABLE IF EXISTS Journals;
/* DROP TABLE IF EXISTS Workouts; */
DROP TABLE IF EXISTS Exercises;
DROP TABLE IF EXISTS Body;

CREATE TABLE Users (
    user_id text PRIMARY KEY,
    email text,
    name text
);

CREATE TABLE Activities (
    activity_id text,
    user_id text,
    exercise_id text,
    timestamp bigint,
    day integer,
    month integer,
    year integer,
    notes text
);

/*
CREATE TABLE Journals (
    user_id text,
    timestamp bigint,
    day integer,
    month integer,
    year integer,
    notes text
);
*/

/*
CREATE TABLE Workouts (
    workout_id text PRIMARY KEY,
    user_id text,
    name text,
    date_created text,
    is_public integer,
    description text
);
*/

CREATE TABLE Exercises (
    exercise_id text PRIMARY KEY,
    user_id text,
    name text,
    category text,
    sets integer,
    reps integer,
    amount integer,
    units text
);

CREATE TABLE Body (
    user_id text,
    date text,
    body_weight integer,
    units text,
    body_fat integer
);

/* Load sample data */
INSERT INTO Users
VALUES ('u001', 'test1@gmail.com', 'test1'), ('u002', 'test2@gmail.com', 'test2'), ('u003', 'test3@gmail.com', 'test3');

INSERT INTO Activities
VALUES
    ('a001', 'u001', 'e001', 1618510614562, 15, 4, 2021, 'test notes 1'),
    ('a003', 'u001', 'e002', 1618510614562, 15, 4, 2021, 'test notes 2'),
    ('a004', 'u002', 'e004', 1604390400000, 3, 10, 2020, 'test notes 3'),
    ('a005', 'u001', 'e003', 1594191600000, 8, 6, 2020, 'test notes 4');

/*
INSERT INTO Journals
VALUES
    ('u001', 1618510614562, 15, 4, 2021, 'test1'),
    ('u001', 15941916000008, 8, 6, 2020, 'test2');
*/

/*
INSERT INTO Workouts
VALUES
    ('w1', 'u001', 'Chest & Arms', '4/01/21', 1, 'Massive chest and arms workout'),
    ('w2', 'u002', 'Back and Abs', '4/02/21', 0, 'Massive back and abs workout'),
    ('w3', 'u001', 'Long Distance Run', '4/03/21', 1, 'Long run');
*/

INSERT INTO Exercises
VALUES
    ('e001', 'u001', 'Bench-press', 'Weight-lifting', 4, 8, 225, 'lbs'),
    ('e002', 'u001', 'Incline-press', 'Weight-lifting', 4, 8, 185, 'lbs'),
    ('e003', 'u001', 'Db flies', 'Weight-lifting', 3, 12, 30, 'lbs'),
    ('e004', 'u002', 'Long Distance Run', 'Cardio', 0, 0, 12, 'miles');

INSERT INTO Body
VALUES
    ('u001', '4/11/21', 176, 'lbs', 15),
    ('u001', '4/23/21', 173, 'lbs', 14.6)

