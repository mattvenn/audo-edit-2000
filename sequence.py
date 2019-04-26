from enum import Enum
class ShotType(Enum):
    title = 1
    speedup = 2
    cut = 3
    end = 4

sequence = [
    {
        "time" : (0,15),
        "type" : ShotType.title,
        "text" : "intro to cover",
    },
    {
        "time" : (0,40),
        "type" : ShotType.title,
        "text" : "testbenches",
    },
    {
        "time" : (1,47),
        "type" : ShotType.title,
        "text" : "makefile",
    },
    # fake
    {
        "time" : (1,50),
        "type" : ShotType.end,
    },
    {
        "time" : (2,9),
        "type" : ShotType.title,
        "text" : "gtkwave",
    },
    {
        "time" : (2,40),
        "type" : ShotType.title,
        "text" : "4 LEDs parameter",
    },
    {
        "time" : (3,10),
        "type" : ShotType.title,
        "text" : "alternative to testbench: cover",
    },
    {
        "time" : (3,21),
        "type" : ShotType.speedup,
        "speed": 5,
    },
    {
        "time" : (4,40),
        "type" : ShotType.title,
        "text" : "the cover statement",
    },
    {
        "time" : (13,13),
        "type" : ShotType.end,
    },
]
"""
4:50,sby config
5:00,makefile
5:22,run cover with sby
5:30,cover fails
6:00,ws2812 long reset time
6:30,change params
6:47,SPEEDUP
7:05,ws2812 timing
7:32,CUT
8:01,webpage...
8:50,cover reached
9:06,SPEEDUP
9:30,makefile ORing
10:00,append
11:15,cover led data
11:50,write signal is now toggling
12:26,2 LEDs
12:45,AABBCC data is seen
12:50,outro
13:10,COMMENTS!!!
"""
