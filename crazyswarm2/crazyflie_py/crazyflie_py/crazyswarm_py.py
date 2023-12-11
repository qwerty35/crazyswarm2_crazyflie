import rclpy

from . import genericJoystick
from .crazyflie import CrazyflieServer, TimeHelper


class Crazyswarm:

    def __init__(self, namespace=''):
        rclpy.init()

        self.allcfs = CrazyflieServer(namespace)
        self.timeHelper = TimeHelper(self.allcfs)

        self.input = genericJoystick.Joystick(self.timeHelper)
