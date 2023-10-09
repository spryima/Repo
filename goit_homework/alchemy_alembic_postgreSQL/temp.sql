
DROP TABLE IF EXISTS groups CASCADE;
CREATE TABLE groups (
    id SMALLSERIAL PRIMARY KEY,
    group_name VARCHAR(255) UNIQUE NOT NULL
);


DROP TABLE IF EXISTS students CASCADE;
CREATE TABLE students (
    id SMALLSERIAL PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(id)
      ON UPDATE CASCADE
);

DROP TABLE IF EXISTS subjects CASCADE;
CREATE TABLE subjects (
    id SMALLSERIAL PRIMARY KEY,
    subj_name VARCHAR(255) NOT NULL UNIQUE
);

DROP TABLE IF EXISTS teachers CASCADE;
CREATE TABLE teachers (
    id SMALLSERIAL PRIMARY KEY,
    teacher_name VARCHAR(255) NOT NULL,
    subj_name_id INTEGER,
    FOREIGN KEY (subj_name_id) REFERENCES subjects(id)
      ON UPDATE CASCADE
);

DROP TABLE IF EXISTS scoreboard CASCADE;
CREATE TABLE scoreboard (
    id SMALLSERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    subj_name VARCHAR(255) NOT NULL,
    grade INTEGER NOT NULL,
    date_received DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subj_name) REFERENCES subjects(subj_name)    
);




