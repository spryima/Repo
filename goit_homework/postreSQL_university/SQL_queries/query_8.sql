SELECT teachers.teacher_name, subjects.subj_name, AVG(scoreboard.grade) AS average_grade
FROM teachers
INNER JOIN subjects ON teachers.subj_name_id = subjects.id
INNER JOIN scoreboard ON subjects.subj_name = scoreboard.subj_name
WHERE teachers.teacher_name = 'Теодор Савенко'
GROUP BY teachers.teacher_name, subjects.subj_name
ORDER BY average_grade DESC;
