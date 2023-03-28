#!/usr/bin/env python

import rospy
from plant_care.srv import CheckMoistureLevel, CheckMoistureLevelResponse

def handle_check_moisture_level(req):
    # TODO: Get the moisture level of the soil and return it in the response
    moisture_level = 50.0  # Dummy value
    return CheckMoistureLevelResponse(moisture_level)

def check_moisture_level_server():
    rospy.init_node('check_moisture_level_server')
    s = rospy.Service('check_moisture_level', CheckMoistureLevel, handle_check_moisture_level)
    print("Ready to check moisture level")
    rospy.spin()

if name == '__main__':
    check_moisture_level_server()
