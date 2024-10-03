MySQL [cell_tower_db]> DESCRIBE Devices;
+----------------+--------------+------+-----+---------+----------------+
| Field          | Type         | Null | Key | Default | Extra          |
+----------------+--------------+------+-----+---------+----------------+
| device_id      | int(11)      | NO   | PRI | NULL    | auto_increment |
| device_imei    | varchar(15)  | NO   | UNI | NULL    |                |
| device_type_id | int(11)      | YES  | MUL | NULL    |                |
| manufacturer   | varchar(100) | YES  |     | NULL    |                |
| model          | varchar(100) | YES  |     | NULL    |                |
| carrier_id     | int(11)      | YES  | MUL | NULL    |                |
+----------------+--------------+------+-----+---------+----------------+
6 rows in set (0.001 sec)

MySQL [cell_tower_db]> DESCRIBE Device_Types;
+------------------+--------------+------+-----+---------+----------------+
| Field            | Type         | Null | Key | Default | Extra          |
+------------------+--------------+------+-----+---------+----------------+
| device_type_id   | int(11)      | NO   | PRI | NULL    | auto_increment |
| device_type_name | varchar(100) | NO   |     | NULL    |                |
+------------------+--------------+------+-----+---------+----------------+
2 rows in set (0.001 sec)

MySQL [cell_tower_db]> select * from Device_Types;
+----------------+---------------------------+
| device_type_id | device_type_name          |
+----------------+---------------------------+
|              1 | smartphone                |
|              2 | mobile phone              |
|              3 | tablet                    |
|              4 | computer                  |
|              5 | iot                       |
|              6 | modem                     |
|              7 | gps fleet tracking device |
|              8 | health monitoring device  |
|              9 | point of sale             |
|             10 | vehicle                   |
+----------------+---------------------------+
10 rows in set (0.001 sec)

MySQL [cell_tower_db]> SELECT COUNT(*) AS device_count
    -> FROM Devices
    -> WHERE device_type_id IN (1, 3, 4);
+--------------+
| device_count |
+--------------+
|          714 |
+--------------+


flag{714}

