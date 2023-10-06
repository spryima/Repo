select group_name, student_name, grade
FROM groups
INNER JOIN students 
ON groups.id = students.group_id
INNER JOIN scoreboard 
ON students.id = scoreboard.student_id
INNER JOIN subjects 
ON scoreboard.subj_name = subjects.subj_name
where groups.group_name = 'lr-14'and subjects.subj_name = 'Фізика';