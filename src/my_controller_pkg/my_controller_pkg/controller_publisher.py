#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32MultiArray

class ControllerPublisher(Node):
    def __init__(self):
        super().__init__('controller_publisher')
        self.joy_subscription = self.create_subscription(
            Joy,
            '/joy',
            self.joy_callback,
            10)
        self.command_publisher = self.create_publisher(
            Float32MultiArray,
            '/controller_commands',
            10)
        self.get_logger().info('Controller publisher node started.')

    def joy_callback(self, msg):
     # fuer PS4-Controller Linker Stick vertikal (Achse 1): Vorwärts (+) / Rückwärts (-) | fuer Xbox-Controller: Linker Stick vertikal (Achse 1): Vorwärts (+) / Rückwärts (-)
     forward_backward = msg.axes[1]

     # fuer PS4-Controller: Rechter Stick horizontal (Achse 2): Rechts (+) / Links (-) | fuer Xbox-Controller: Rechter Stick horizontal (Achse 3): Rechts (+) / Links (-)
     turn =-msg.axes[2]

     # Erstelle eine Nachricht mit den Steuerbefehlen
     command_msg = Float32MultiArray()
     command_msg.data = [forward_backward, turn]

     # Veröffentliche die Nachricht
     self.command_publisher.publish(command_msg)
     self.get_logger().info(f'Published commands: Forward/Backward={forward_backward:.2f}, Turn={turn:.2f}')

def main(args=None):
    rclpy.init(args=args)
    controller_publisher = ControllerPublisher()
    rclpy.spin(controller_publisher)
    controller_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
