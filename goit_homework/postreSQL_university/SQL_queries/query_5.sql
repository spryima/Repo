SELECT teacher_name, subj_name
FROM teachers
INNER JOIN subjects s 
ON teachers.subj_name_id = s.id 
WHERE teacher_name = 'Теодор Савенко';