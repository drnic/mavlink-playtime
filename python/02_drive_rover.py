from dronekit import connect, VehicleMode
from pymavlink import mavutil
from geopy import distance

import copy
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--connect',
                    help='Connection string to MAVLink, default udp:127.0.0.1:14550',
                    default='udp:127.0.0.1:14550')
args = parser.parse_args()

print(">>>> Connecting with the UAV <<<")
# vehicle = connect(connection_string, wait_ready=True)     #- wait_ready flag hold the program untill all the parameters are been read (=, not .)
vehicle = connect(args.connect, wait_ready=True)

vehicle.wait_ready('autopilot_version')

if vehicle.version.vehicle_type != mavutil.mavlink.MAV_TYPE_GROUND_ROVER:
    print("ERROR: this script assumes drone is a Rover")
    exit

cmds = vehicle.commands
cmds.download()
cmds.wait_ready()
print(" Home Location: %s" % vehicle.home_location)

drive_to = copy.copy(vehicle.home_location)
drive_to.lon += 0.01
drive_distance = distance.distance(
                    (vehicle.home_location.lat,vehicle.home_location.lon),
                    (drive_to.lat, drive_to.lon)).nm
print(" Drive To: %s (Distance: %.2f nm)" % (drive_to, drive_distance))

vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True
while not vehicle.mode.name=='GUIDED' and not vehicle.armed:
    print(" Getting ready to take off ...")
    time.sleep(1)

print(" Driving...")
vehicle.airspeed = 5 #m/s
vehicle.simple_goto(drive_to)
