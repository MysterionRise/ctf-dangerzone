Access the database via SSH at skywave.deadface.io.
Username: skywave
Password: d34df4c3


MySQL [cell_tower_db]> SELECT device_id, COUNT(DISTINCT tower_id) AS unique_tower_count
    -> FROM Connections
    -> WHERE connection_time BETWEEN '2024-09-07 16:10:00' AND '2024-09-07 18:54:00'
    -> GROUP BY device_id
    -> ORDER BY unique_tower_count DESC
    -> LIMIT 1;
+-----------+--------------------+
| device_id | unique_tower_count |
+-----------+--------------------+
|      2325 |                  5 |
+-----------+--------------------+
1 row in set (0.006 sec)


SELECT device_imei 
FROM Devices 
WHERE device_id = 2325;