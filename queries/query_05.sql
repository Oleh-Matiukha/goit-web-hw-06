SELECT sub.name
FROM subjects sub
JOIN teachers t ON sub.teacher_id = t.id
WHERE t.id = 1;  -- Замініть 1 на ID викладача