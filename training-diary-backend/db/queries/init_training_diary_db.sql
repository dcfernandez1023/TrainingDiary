DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Exercises;
DROP TABLE IF EXISTS ExerciseEntries;
DROP TABLE IF EXISTS BodyWeight;
DROP TABLE IF EXISTS BodyFat;
DROP TABLE IF EXISTS Diet;
DROP TABLE IF EXISTS CustomTypes;
DROP TABLE IF EXISTS CustomEntries;

CREATE TABLE Users (
    user_id text PRIMARY KEY,
    email text,
    name text
);

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

CREATE TABLE ExerciseEntries (
    exercise_entry_id text PRIMARY KEY,
    exercise_id text,
    user_id text,
    timestamp bigint,
    day integer,
    month integer,
    year integer,
    notes text
);

CREATE TABLE BodyWeight (
    bw_id text PRIMARY KEY,
    user_id text,
    weight integer,
    units text,
    timestamp bigint,
    day integer,
    month integer,
    year integer,
    notes text
);

CREATE TABLE BodyFat (
    bf_id text PRIMARY KEY,
    user_id text,
    percentage integer,
    timestamp bigint,
    day integer,
    month integer,
    year integer,
    notes text
);

CREATE TABLE Diet (
    user_id text,
    day integer,
    month integer,
    year integer,
    calories integer,
    protein integer,
    carbs integer,
    fat integer,
    notes text,
    PRIMARY KEY(user_id, day, month, year)
);

CREATE TABLE CustomTypes (
    custom_id text PRIMARY KEY,
    user_id text,
    custom_schema json
);

CREATE TABLE CustomEntries (
    custom_entry_id text PRIMARY KEY,
    custom_id text,
    user_id text,
    custom_entry json,
    timestamp bigint,
    day integer,
    month integer,
    year integer,
    notes text
);


/* Load sample data */
INSERT INTO Users
VALUES ('u001', 'test1@gmail.com', 'test1'), ('u002', 'test2@gmail.com', 'test2'), ('u003', 'test3@gmail.com', 'test3');

INSERT INTO Exercises
VALUES
    ('e001', 'u001', 'Bench-press', 'Weight-lifting', 4, 8, 225, 'lbs'),
    ('e002', 'u001', 'Incline-press', 'Weight-lifting', 4, 8, 185, 'lbs'),
    ('e003', 'u001', 'Db flies', 'Weight-lifting', 3, 12, 30, 'lbs'),
    ('e004', 'u002', 'Long Distance Run', 'Cardio', 0, 0, 12, 'miles');

INSERT INTO ExerciseEntries
VALUES
    ('ee001', 'e001', 'u001', 1618637490472, 16, 4, 2021, 'test1'),
    ('ee002', 'e002', 'u001', 1447920000000, 19, 10, 2015, 'test2'),
    ('ee003', 'e003', 'u001', 1618637490472, 16, 4, 2021, 'test3'),
    ('ee004', 'e004', 'u002', 1618637490472, 16, 4, 2021, 'test4');

INSERT INTO BodyWeight
VALUES
    ('bw001', 'u001', 177, 'lbs', 1618637490472, 16, 4, 2021, 'yoo'),
    ('bw002', 'u001', 176, 'lbs', 1649055600000, 15, 4, 2021, 'dawg');

INSERT INTO BodyFat
VALUES
    ('bf001', 'u001', 15, 1618637490472, 16, 4, 2021, 'gotta get this lower'),
    ('bf002', 'u001', 14.8, 1649055600000, 15, 4, 2021, 'testseteststs');

INSERT INTO Diet
VALUES
    ('u001', 16, 4, 2021, 2700, 180, 230, 82, 'hit goals today'),
    ('u001', 15, 4, 2021, 2700, 178, 214, 85, 'hit goals today again');

INSERT INTO CustomTypes
VALUES
    ('c001', 'u001', '{"name": "Sleep", "hours": 0}');

INSERT INTO CustomEntries
VALUES
    ('ce001', 'c001', 'u001', '{"name": "Sleep", "hours": 7}', 1618637490472, 16, 4, 2021, 'testing custom entries');
