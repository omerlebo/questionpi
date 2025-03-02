CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    difficulty VARCHAR(10) NOT NULL,
    category VARCHAR(50) NOT NULL,
    question TEXT NOT NULL,
    correct_answer TEXT NOT NULL
);

CREATE TABLE question_answers (
    id SERIAL PRIMARY KEY,
    question_id INT NOT NULL,
    answer TEXT NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
);