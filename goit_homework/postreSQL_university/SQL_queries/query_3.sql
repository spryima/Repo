SELECT groups.group_name, subjects.subj_name, AVG(scoreboard.grade) AS average_grade
FROM groups
INNER JOIN students 
ON groups.id = students.group_id
INNER JOIN scoreboard 
ON students.id = scoreboard.student_id
INNER JOIN subjects 
ON scoreboard.subj_name = subjects.subj_name
WHERE subjects.subj_name = 'Фізика'
GROUP BY groups.group_name, subjects.subj_name
ORDER BY average_grade DESC;