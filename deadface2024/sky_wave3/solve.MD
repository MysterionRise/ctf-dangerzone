SELECT a.antenna_name, COUNT(*) AS antenna_count
FROM Antennas a
JOIN Tower_Sectors ts ON a.antenna_id = ts.antenna_id
JOIN Towers t ON ts.tower_id = t.tower_id
WHERE t.operator_id = (SELECT operator_id FROM Operators WHERE first_name = 'Florian' AND last_name = 'Olyff')
GROUP BY a.antenna_name
ORDER BY antenna_count DESC
LIMIT 1;

