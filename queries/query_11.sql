SELECT s.fullname, ROUND(AVG(gr.grade), 2) AS average_grade
FROM grades gr
JOIN subjects sub ON gr.subject_id = sub.id
JOIN students s ON gr.student_id = s.id
WHERE s.id = 1  -- Замініть 1 на ID студента
AND sub.teacher_id = 1  -- Замініть 1 на ID викладача
GROUP BY s.id;
