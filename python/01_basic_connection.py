from dronekit import connect, VehicleMode
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--connect',
                    help='Connection string to MAVLink',
                    default='udp:127.0.0.1:14550')
args = parser.parse_args()

print(">>>> Connecting with the UAV <<<")
# vehicle = connect(connection_string, wait_ready=True)     #- wait_ready flag hold the program untill all the parameters are been read (=, not .)
vehicle = connect(args.connect)

vehicle.wait_ready('autopilot_version')
print('Autopilot version: %s' % vehicle.version)
