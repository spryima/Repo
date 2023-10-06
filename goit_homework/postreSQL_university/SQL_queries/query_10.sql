select distinct subjects.subj_name
FROM students
INNER JOIN scoreboard 
ON students.id = scoreboard.student_id
INNER JOIN subjects 
ON scoreboard.subj_name = subjects.subj_name
INNER JOIN teachers 
ON subjects.id = teachers.subj_name_id
WHERE students.student_name = 'Хома Остапчук' 
AND teachers.teacher_name = 'Теодор Савенко'
ORDER BY subjects.subj_name;