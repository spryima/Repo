SELECT group_name, student_name
FROM groups
inner join students s  
on groups.id = s.group_id 
order by group_name;