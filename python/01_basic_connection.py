from dronekit import connect, VehicleMode
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

print("Autopilot Firmware version: %s" % vehicle.version)
print("Autopilot capabilities (supports ftp): %s" % vehicle.capabilities.ftp)
print("Global Location: %s" % vehicle.location.global_frame)
print("Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
print("Local Location: %s" % vehicle.location.local_frame)    #NED
print("Attitude: %s" % vehicle.attitude)
print("Velocity: %s" % vehicle.velocity)
print("GPS: %s" % vehicle.gps_0)
print("Groundspeed: %s" % vehicle.groundspeed)
print("Airspeed: %s" % vehicle.airspeed)
print("Gimbal status: %s" % vehicle.gimbal)
print("Battery: %s" % vehicle.battery)
print("EKF OK?: %s" % vehicle.ekf_ok)
print("Last Heartbeat: %s" % vehicle.last_heartbeat)
print("Rangefinder: %s" % vehicle.rangefinder)
print("Rangefinder distance: %s" % vehicle.rangefinder.distance)
print("Rangefinder voltage: %s" % vehicle.rangefinder.voltage)
print("Heading: %s" % vehicle.heading)
print("Is Armable?: %s" % vehicle.is_armable)
print("System status: %s" % vehicle.system_status.state)
print("Mode: %s" % vehicle.mode.name)    # settable
print("Armed: %s" % vehicle.armed)       # settable
