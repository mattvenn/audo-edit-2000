from enum import Enum
class ShotType(Enum):
    title = 1
    speedup = 2
    cut = 3
    end = 4

sequence = [
    {
        "time" : (0,12),
        "type" : ShotType.title,
        "text" : "intro to cover",
    },
    {
        "time" : (0,40),
        "type" : ShotType.title,
        "text" : "testbenches",
    },
    {
        "time" : (1,45),
        "type" : ShotType.title,
        "text" : "makefile",
    },
    {
        "time" : (2,3),
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
        "speed": 2.5,
    },
    {
        "time" : (4,33),
        "type" : ShotType.title,
        "text" : "the cover statement",
    },
    {
        "time" : (4,48),
        "type" : ShotType.title,
        "text" : "sby config",
    },
    {
        "time" : (5,0),
        "type" : ShotType.title,
        "text" : "makefile",
    },
    {
        "time" : (5,22),
        "type" : ShotType.title,
        "text" : "run cover with sby",
    },
    {
        "time" : (5,30),
        "type" : ShotType.title,
        "text" : "cover fails",
    },
    {
        "time" : (6,0),
        "type" : ShotType.title,
        "text" : "ws2812 long reset time",
    },
    {
        "time" : (6,30),
        "type" : ShotType.title,
        "text" : "change params",
    },
    {
        "time" : (6,30),
        "type" : ShotType.speedup,
        "speed" : 5,
    },
    {
        "time" : (7,05),
        "type" : ShotType.title,
        "text" : "ws2812 timing",
    },
    {
        "time" : (7,32),
        "type" : ShotType.cut,
    },
    {
        "time" : (8,1),
        "type" : ShotType.title,
        "text" : "webpage...",
    },
    {
        "time" : (8,50),
        "type" : ShotType.title,
        "text" : "cover reached",
    },
    {
        "time" : (9,9),
        "type" : ShotType.speedup,
        "speed" : 3,
    },
    {
        "time" : (9,24),
        "type" : ShotType.title,
        "text" : "makefile ORing",
    },
    {
        "time" : (10,0),
        "type" : ShotType.title,
        "text" : "append steps",
    },
    {
        "time" : (11,15),
        "type" : ShotType.title,
        "text" : "cover LED data",
    },
    {
        "time" : (11,50),
        "type" : ShotType.title,
        "text" : "write signal is now toggling",
    },
    {
        "time" : (12,26),
        "type" : ShotType.title,
        "text" : "2 LEDs",
    },
    {
        "time" : (12,45),
        "type" : ShotType.title,
        "text" : "AABBCC data is seen",
    },
    {
        "time" : (12,50),
        "type" : ShotType.title,
        "text" : "outro",
    },
    {
        "time" : (13,8),
        "type" : ShotType.title,
        "text" : "COMMENTS!!!",
    },
    {
        "time" : (13,15),
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
