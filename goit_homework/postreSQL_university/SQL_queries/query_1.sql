SELECT student_name, AVG(grade) AS average_grade
FROM students  
INNER JOIN scoreboard 
ON students.id = scoreboard.student_id 
GROUP BY student_name
ORDER BY average_grade DESC
LIMIT 5;