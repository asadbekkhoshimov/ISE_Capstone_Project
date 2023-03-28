#!/usr/bin/env python

import rospy
import actionlib
from plant_care.msg import WaterPlantAction, WaterPlantResult

class WaterPlantServer(object):

    def __init__(self):
        self._as = actionlib.SimpleActionServer('water_plant', WaterPlantAction, self.execute, False)
        self._as.start()

    def execute(self, goal):
        # TODO: Water the plant and return the result
        success = True  # Dummy value
        if success:
            self._as.set_succeeded(WaterPlantResult(True))
        else:
            self._as.set_aborted()

if name == '__main__':
    rospy.init_node('water_plant_server')
    server = WaterPlantServer()
    rospy.spin()
