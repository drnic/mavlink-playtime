# MAVLink Playtime in Python

In lieu of a real drone, perhaps run the Software-in-the-loop (SITL). I wrote up some instructions for Vagrant/MacOS at https://discuss.ardupilot.org/t/tutorial-for-running-sitl-simulator-on-macos-with-vagrant-xquartz/38383

The code examples assume Python 3+. To install dependencies:

```plain
cd python
pip3 install -r requirements.txt
```

Simple test of connection over MAVLink:

```plain
python3 01_basic_connection.py
```

By default it attempts to connect on `udp:127.0.0.1:14550`. You can specify a different string with `-c` or `--connect`.

See http://python.dronekit.io/guide/connecting_vehicle.html for more examples of connection strings.

The next script assumes you're vehicle/SITL is a Rover. It will get the home location and guide the rover to a point 1/5 nm to the east.

```plain
python3 02_drive_rover.py
>>>> Connecting with the UAV <<<
 Home Location: LocationGlobal:lat=-26.583528518676758,lon=151.84043884277344,alt=-0.10000000149011612
 Drive To: LocationGlobal:lat=-26.583528518676758,lon=151.85043884277343,alt=-0.10000000149011612 (Distance: 0.54 nm)
 Driving...
```

![02-rover](https://cl.ly/21d716619fe6/download/rover-driving.png)
