from enum import Enum
class ShotType(Enum):
    title = 1
    speedup = 2
    cut = 3
    end = 4

sequence = [
    {
        "time" : (7,05),
        "type" : ShotType.title,
        "text" : "ws2812 parameters",
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
        "time" : (9,06),
        "type" : ShotType.speedup,
        "speed" : 5,
    },
    {
        "time" : (9,25),
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
        "time" : (13,10),
        "type" : ShotType.title,
        "text" : "COMMENTS!!!",
    },
    {
        "time" : (13,15),
        "type" : ShotType.end,
    },
]
