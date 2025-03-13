SELECT s.id, s.fullname, gr.grade
FROM grades gr
JOIN students s ON gr.student_id = s.id
WHERE s.group_id = 1  -- Замініть 1 на ID групи
AND gr.subject_id = 1;  -- Замініть 1 на ID предмета
