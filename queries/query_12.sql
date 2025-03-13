WITH LastGrades AS (
    SELECT student_id, subject_id, MAX(grade_date) AS last_grade_date
    FROM grades
    GROUP BY student_id, subject_id
)
SELECT s.fullname, gr.grade, gr.grade_date
FROM grades gr
JOIN students s ON gr.student_id = s.id
JOIN subjects sub ON gr.subject_id = sub.id
JOIN LastGrades lg ON gr.student_id = lg.student_id
                AND gr.subject_id = lg.subject_id
                AND gr.grade_date = lg.last_grade_date
WHERE s.group_id = 1  -- Замініть 1 на ID групи
AND sub.id = 1;  -- Замініть 1 на ID предмета
