Access the database via SSH at skywave.deadface.io.
Username: skywave
Password: d34df4c3

SELECT tower_id 
    -> FROM Towers 
    -> WHERE (latitude = 41.639642 AND longitude = -79.220682)
    ->    OR (latitude = 40.598271 AND longitude = -78.801089)
    ->    OR (latitude = 41.045892 AND longitude = -79.068358)
    ->    OR (latitude = 41.257279 AND longitude = -77.529468);
+----------+
| tower_id |
+----------+
|      105 |
|      123 |
|      187 |
|      200 |
+----------+

SELECT device_id, connection_duration 
    -> FROM Connections 
    -> WHERE tower_id IN (105, 123, 187, 200)
    -> AND signal_strength > -100
    -> ORDER BY connection_duration DESC
    -> LIMIT 1;

+-----------+---------------------+
| device_id | connection_duration |
+-----------+---------------------+
|       344 |               85709 |
+-----------+---------------------+

select device_imei from Devices where device_id=344;
+-----------------+
| device_imei     |
+-----------------+
| 845303290931675 |
+-----------------+

