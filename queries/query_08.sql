SELECT t.id, t.fullname, ROUND(AVG(gr.grade), 2) AS average_grade
FROM grades gr
JOIN subjects sub ON gr.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
WHERE t.id = 1  -- Замініть 1 на ID викладача
GROUP BY t.id;