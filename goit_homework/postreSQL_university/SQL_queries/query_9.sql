SELECT DISTINCT subjects.subj_name
FROM students
INNER JOIN scoreboard 
ON students.id = scoreboard.student_id
INNER JOIN subjects 
ON scoreboard.subj_name = subjects.subj_name
WHERE students.student_name = 'Хома Остапчук'