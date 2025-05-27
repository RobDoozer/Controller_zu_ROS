Hier ist eine Zusammenfassung der Befehle, die du auf einem anderen PC ausführen musst, um deinen ROS 2 Code von GitHub zum Laufen zu bringen:1. ROS 2 Installation (falls noch nicht vorhanden):Installiere ROS 2 Humble Hawksbill gemäß der offiziellen Anleitung für dein Betriebssystem.2. ROS 2 Workspace einrichten:mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
3. Code von GitHub klonen:git clone https://github.com/RobDoozer/Controller_zu_ROS.git
4. Zum Workspace-Root wechseln:cd ~/ros2_ws
5. ROS 2 Paket bauen:colcon build
6. ROS 2 Umgebung sourcen (in JEDEM neuen Terminal):source install/setup.bash
7. PS4-Controller anschließen und joy_node starten (in einem Terminal mit gesourcter Umgebung):ros2 run joy joy_node
8. Deinen controller_publisher Node starten (in einem weiteren Terminal mit gesourcter Umgebung):ros2 run my_controller_pkg controller_publisher
9. (Optional) Controller-Befehle beobachten (in einem dritten Terminal mit gesourcter Umgebung):ros2 topic echo /controller_commands
