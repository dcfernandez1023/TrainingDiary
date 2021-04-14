DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Activities;
DROP TABLE IF EXISTS Workouts;
DROP TABLE IF EXISTS Exercises;
DROP TABLE IF EXISTS Body;

CREATE TABLE Users (
    user_id text PRIMARY KEY,
    email text,
    name text
);

CREATE TABLE Activities (
    user_id text,
    workout_id text,
    date text
);

CREATE TABLE Workouts (
    workout_id text PRIMARY KEY,
    user_id text,
    name text,
    date_created text,
    is_public integer,
    description text
);

CREATE TABLE Exercises (
    workout_id text,
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
VALUES ('u001', 'w1', '4/11/21'), ('u001', 'w3', '4/10/21'), ('u002', 'w2', '4/7/21'), ('u001', 'w1', '4/6/21');

INSERT INTO Workouts
VALUES
    ('w1', 'u001', 'Chest & Arms', '4/1/21', 1, 'Massive chest and arms workout'),
    ('w2', 'u002', 'Back and Abs', '4/2/21', 0, 'Massive back and abs workout'),
    ('w3', 'u001', 'Long Distance Run', '4/3/21', 1, 'Long run');

INSERT INTO Exercises
VALUES
    ('w1', 'u001', 'Bench-press', 'Weight-lifting', 4, 8, 225, 'lbs'),
    ('w1', 'u001', 'Incline-press', 'Weight-lifting', 4, 8, 185, 'lbs'),
    ('w1', 'u001', 'Db flies', 'Weight-lifting', 3, 12, 30, 'lbs');

INSERT INTO Body
VALUES
    ('u001', '4/11/21', 176, 'lbs', 15),
    ('u001', '4/23/21', 173, 'lbs', 14.6)

