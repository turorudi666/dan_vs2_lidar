# LiDAR akadályérzékelő

ROS 2 alapú LiDAR akadályérzékelő projekt Python nyelven.

## Projekt leírása

A projekt célja LiDAR szenzoradatok szimulálása, valamint a robot előtti akadályok érzékelése.

A projekt két ROS 2 node-ból fog állni:

- `lidar_simulator` – szimulált LiDAR méréseket publikál `sensor_msgs/LaserScan` üzenettípussal.
- `obstacle_detector` – feliratkozik a LiDAR adatokra, és meghatározza, hogy található-e túl közeli akadály a robot előtt.

Az akadályérzékelő három állapotot fog használni:

- `CLEAR` – nincs közeli akadály
- `WARNING` – akadály található a robot közelében
- `STOP` – az akadály kritikus távolságon belül van

## Használt technológiák

- ROS 2 Humble
- Python
- `rclpy`
- `sensor_msgs`
- `std_msgs`
