
config = {
    'files': 
    {
            'webcam' :
            { 
                'file' : 'cover-webcam.mkv', #  1280 x 800
                'start': 0,
                'audio': True,
            },
            'screen' :
            {
                'file' :'cover-screen.mkv', # 800 x 600
                'start': 2,
                'audio': False,
            },
    },
#        'pic1'   : 'test.png',
    'sequence_defaults' :
    {
        "comp" : [ 'screen', 'webcam' ],
        'clip_size' : { 'webcam' : 400, 'screen' : 1280 }, # desired width of video clips
        'clip_pos' : { 'webcam' : (1280 - 400, 0), 'screen' : (0,0) },
        "text" : None,
        "title_duration" : 5,
        "speed": 1,
    },
    'sequence' : [
    {
        "time" : (0,12),
        "comp" : [ "screen", "webcam" ],
        "clip_size" : { 'webcam' : 800, 'screen' : 1280 },
        "clip_pos" : { 'webcam' : ((1280 - 800)/2, (800-600)/2), 'screen': (0,0) },
        "text" : "intro to cover",
    },
    {
        "time" : (0,40),
        "text" : "github.com/mattvenn/ws2812-core",
    },
    {
        "time" : (1,45),
        "clips" : [ "screen" ],
        "speed": 5,
        "text" : "makefile",
    },
    {
        "time" : (2,3),
        "text" : "gtkwave",
    },
#    {
#        "time" : (2,40),
#        "type" : "title",
#        "text" : "4 LEDs parameter",
#    },
#    {
#        "time" : (3,10),
#        "type" : "title",
#        "text" : "alternative to testbench: cover",
#    },
#    {
#        "time" : (3,21),
#        "type" : "speedup",
#        "speed": 2.5,
#    },
#    {
#        "time" : (4,33),
#        "type" : "title",
#        "text" : "the cover statement",
#    },
#    {
#        "time" : (4,48),
#        "type" : "title",
#        "text" : "sby config",
#    },
#    {
#        "time" : (5,0),
#        "type" : "title",
#        "text" : "makefile",
#    },
#    {
#        "time" : (5,22),
#        "type" : "title",
#        "text" : "run cover with sby",
#    },
#    {
#        "time" : (5,30),
#        "type" : "title",
#        "text" : "cover fails",
#    },
#    {
#        "time" : (6,0),
#        "type" : "title",
#        "text" : "ws2812 long reset time",
#    },
#    {
#        "time" : (6,30),
#        "type" : "speedup",
#        "speed" : 5,
#    },
#    {
#        "time" : (7,05),
#        "type" : "title",
#        "text" : "ws2812 timing",
#    },
#    {
#        "time" : (7,32),
#        "type" : "cut",
#    },
#    {
#        "time" : (8,1),
#        "type" : "title",
#        "text" : "webpage...",
#    },
#    {
#        "time" : (8,50),
#        "type" : "title",
#        "text" : "cover reached",
#    },
#    {
#        "time" : (9,9),
#        "type" : "speedup",
#        "speed" : 3,
#    },
#    {
#        "time" : (9,24),
#        "type" : "title",
#        "text" : "makefile ORing",
#    },
#    {
#        "time" : (10,0),
#        "type" : "title",
#        "text" : "append steps",
#    },
#    {
#        "time" : (11,15),
#        "type" : "title",
#        "text" : "cover LED data",
#    },
#    {
#        "time" : (11,50),
#        "type" : "title",
#        "text" : "write signal is now toggling",
#    },
#    {
#        "time" : (12,26),
#        "type" : "title",
#        "text" : "2 LEDs",
#    },
#    {
#        "time" : (12,45),
#        "type" : "title",
#        "text" : "AABBCC data is seen",
#    },
#    {
#        "time" : (12,50),
#        "type" : "title",
#        "text" : "outro",
#    },
#    {
#        "time" : (13,8),
#        "type" : "title",
#        "text" : "COMMENTS!!!",
#    },
    {
        "time" : (13,15),
        "comp" : [],
    },
    ]
}
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
