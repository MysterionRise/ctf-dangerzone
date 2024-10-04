Access the database via SSH at skywave.deadface.io.
Username: skywave
Password: d34df4c3

MySQL [cell_tower_db]> SELECT c1.device_id, COUNT(*) AS switch_count, MIN(c1.connection_time) AS earliest_time
    -> FROM Connections c1
    -> JOIN Connections c2 ON c1.device_id = c2.device_id 
    -> AND c1.connection_id <> c2.connection_id 
    -> AND c1.tower_id <> c2.tower_id 
    -> AND TIMESTAMPDIFF(MINUTE, c1.connection_time, c2.connection_time) BETWEEN 5 AND 10
    -> GROUP BY c1.device_id
    -> ORDER BY earliest_time ASC
    -> LIMIT 1;
+-----------+--------------+---------------------+
| device_id | switch_count | earliest_time       |
+-----------+--------------+---------------------+
|      1800 |            1 | 2024-09-06 12:27:50 |
+-----------+--------------+---------------------+
1 row in set (0.024 sec)

SELECT device_imei 
FROM Devices 
WHERE device_id = 1800