# MAVLink Playtime in Python

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
