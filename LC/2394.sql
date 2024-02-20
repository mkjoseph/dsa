SELECT e.employee_id
FROM Employees e 
LEFT JOIN (
    SELECT employee_id, 
           SUM(CEIL(TIMESTAMPDIFF(MINUTE, in_time, out_time) / 60.0)) AS total_hours_worked
    FROM Logs
    GROUP BY employee_id
) l ON e.employee_id = l.employee_id
WHERE l.total_hours_worked < e.needed_hours
   OR l.total_hours_worked IS NULL; 
