Access the database via SSH at skywave.deadface.io.
Username: skywave
Password: d34df4c3


ssh skywave@skywave.deadface.io
The authenticity of host 'skywave.deadface.io (68.183.137.215)' can't be established.
ED25519 key fingerprint is SHA256:2fnu0gzMRT4c/l73QWN1CADTsaLJc6SIfMJh+BGiX70.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'skywave.deadface.io' (ED25519) to the list of known hosts.
skywave@skywave.deadface.io's password: 
Linux dctf24-env1 6.1.0-26-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.112-1 (2024-09-30) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Fri Oct 18 14:35:21 2024 from 39.124.25.212
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 247
Server version: 5.7.44 MySQL Community Server (GPL)

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [cell_tower_db]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| cell_tower_db      |
+--------------------+
2 rows in set (0.001 sec)

MySQL [cell_tower_db]> USE cell_tower_db
Database changed
MySQL [cell_tower_db]> SHOW TABLES;
+-------------------------+
| Tables_in_cell_tower_db |
+-------------------------+
| Antennas                |
| Carriers                |
| Connections             |
| Device_Types            |
| Devices                 |
| Operators               |
| Technicians             |
| Tower_Maintenance       |
| Tower_Sectors           |
| Towers                  |
+-------------------------+
10 rows in set (0.001 sec)

MySQL [cell_tower_db]> DESCRIBE Towers;
+-----------------------+---------------------------------+------+-----+---------+----------------+
| Field                 | Type                            | Null | Key | Default | Extra          |
+-----------------------+---------------------------------+------+-----+---------+----------------+
| tower_id              | int(11)                         | NO   | PRI | NULL    | auto_increment |
| location_name         | varchar(255)                    | NO   |     | NULL    |                |
| latitude              | decimal(9,6)                    | NO   |     | NULL    |                |
| longitude             | decimal(9,6)                    | NO   |     | NULL    |                |
| elevation             | decimal(5,2)                    | YES  |     | NULL    |                |
| tower_height          | decimal(5,2)                    | YES  |     | NULL    |                |
| operator_id           | int(11)                         | YES  | MUL | NULL    |                |
| status                | enum('active','decommissioned') | YES  |     | active  |                |
| install_date          | date                            | YES  |     | NULL    |                |
| last_maintenance_date | date                            | YES  |     | NULL    |                |
+-----------------------+---------------------------------+------+-----+---------+----------------+
10 rows in set (0.001 sec)

MySQL [cell_tower_db]> SELECT tower_id, elevation 
    -> FROM Towers 
    -> WHERE elevation BETWEEN 215 AND 225;
+----------+-----------+
| tower_id | elevation |
+----------+-----------+
|       25 |    216.58 |
|       60 |    217.95 |
|      107 |    215.88 |
|      113 |    223.01 |
|      153 |    216.00 |
|      154 |    217.42 |
|      215 |    220.32 |
+----------+-----------+
7 rows in set (0.001 sec)

MySQL [cell_tower_db]> 

flag{215}

flag{ar3_we_410N3??}