SELECT DISTINCT sub.id AS subject_id, sub.name AS subject_name
FROM subjects sub
JOIN grades gr ON sub.id = gr.subject_id
JOIN students s ON gr.student_id = s.id
WHERE s.id = 1  -- Замініть 1 на ID студента
AND sub.teacher_id = 1;  -- Замініть 1 на ID викладача
