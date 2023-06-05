#!/usr/bin/env python
import time
from flyt_python import api
drone = api.navigation(timeout=120000) # instance of flyt droneigation class

#at least 3sec sleep time for the drone interface to initialize properly
time.sleep(3)

print 'Arming'
drone.arm()

print 'taking off'
drone.take_off(5.0)

print 'going along the setpoints'
drone.position_set(6.5,0,0,relative=True)
print 'Reched waypoint 1, heading to next waypoint' #Reached WP1 successfully

drone.position_set(0,6.5,0,relative=True)
print 'Reched waypoint 2, heading to next waypoint' #Reached WP2 successfully

drone.position_set(-6.5,0,0,relative=True)
print 'Reched waypoint 3, heading to next waypoint' #Reached WP3 successfully

drone.position_set(0,-6.5,0,relative=True)
print 'Reched waypoint 4, heading to next waypoint' #Reached WP4 successfully

#triggering Land sequence 
drone.land(async=False)
print 'Landed'

print 'Disarming'
drone.disarm()

#shutdown the instance
drone.disconnect()