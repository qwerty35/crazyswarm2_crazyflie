import rclpy

from . import genericJoystick
from .crazyflie import CrazyflieServer, TimeHelper


class Crazyswarm:

    def __init__(self, cfnames, namespace=''):
        rclpy.init()

        self.allcfs = CrazyflieServer(cfnames, namespace)
        self.timeHelper = TimeHelper(self.allcfs)

        self.input = genericJoystick.Joystick(self.timeHelper)
