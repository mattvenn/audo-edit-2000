config = {
    'outfile': 'cover/cover.mp4',
    'files': 
    {
            'webcam' :
            { 
                'type' : 'video',
                'file' : 'cover/cover-webcam.mkv', #  1280 x 800
                'start': 0,
                'audio': 'cover/cover-webcam.wav',
                'audio_offset' : 0.25,  # 0.25s out - vlc adjusted -0.25s (hastened)
            },
            'screen' :
            {
                'type' : 'video',
                'file' : 'cover/cover-screen.mkv', # 800 x 600
                'start': 1.5,
                'audio': False,
            },
            'background'   :
            {
                'file' : 'cover/ice40-die.jpeg',
                'type' : 'image',
            },
            'intro' :
            {
                'type' : 'video',
                'file' : 'cover/symbiotic-intro.mp4', # 1280 x 800
                'start': 0,
                'audio': False,
            },
    },
    'sequence_defaults' :
    {
        "comp" : [ 'screen', 'webcam' ],
        'clip_size' : { 'intro': (1280,800), 'webcam' : (400,300), 'screen' : (1280,800), 'background' : (1280,800) }, # desired width of video clips
        'clip_pos' : { 'intro' : (0,0), 'webcam' : (1280 - 400, 0), 'screen' : (0,0), 'background' : (0,0) },
        "text" : None,
        "text_vpos" : "top",
        "text_size" : 50,
        "text_duration" : 5, # how long to show texts
        "text_fade_duration" : 0.4, # how long to fade in and out the texts
        "duration" : 0, # duration of the final clip
        "show_text" : False,
        "speed": 1,
        "end" : (0,0),
    },
    ##########################################################
    'sequence' : [
    {
        "time" : (0,0),
        "end"  : (0,3),
        "comp" : [ "intro" ],
    },
    {
        "time" : (0,12),
        "comp" : [ "background", "webcam" ],
        "clip_size" : { 'webcam' : (800,600), 'background' : (1280,800) },
        "clip_pos" : { 'webcam' : ((1280 - 800)/2, (800-600)/2), 'background': (0,0) },
        "text" : "intro to cover",
        "show_text": True,
    },
    {
        "time" : (0,40),
        "text" : "github.com/mattvenn/ws2812-core",
        "show_text": True,
    },
    {
        "time" : (1,45),
        "text" : "makefile",
    },
    {
        "time" : (2,3),
        "text" : "gtkwave",
    },
    {
        "time" : (2,35),
        "text" : "4 LEDs parameter",
    },
    {
        "time" : (3,10),
        "text" : "alternative to testbench: cover",
    },
    {
        "time" : (3,21),
        "comp" : [ "screen" ],
        "speed" : 2.5,
        "text": "adding cover: 2.5x speed",
        "show_text": True,
    },
    {
        "time" : (4,33),
        "text" : "the cover statement",
    },
    {
        "time" : (4,48),
        "text" : "sby config",
    },
    {
        "time" : (5,0),
        "text" : "makefile",
    },
    {
        "time" : (5,14),
        "text" : "run cover with sby",
    },
    {
        "time" : (5,24),
        "text" : "cover fails",
    },
    {
        "time" : (6,0),
        "text" : "ws2812 long reset time",
    },
    {
        "time" : (6,30),
        "comp" : [ "screen" ],
        "text" : "adjust parameters: 5x speed",
        "speed" : 5,
        "show_text": True,
    },
    {
        "time" : (7,5),
        "text" : "ws2812 timing",
    },
    {
        "time" : (7,32),
        "comp" : None,
    },
    {
        "time" : (8,1),
        "text" : "webpage...",
    },
    {
        "time" : (8,55),
        "text" : "cover reached",
    },
    {
        "time" : (9,9),
        "comp" : [ "screen" ],
        "text" : "where did that trace get written? 3x speed",
        "text_vpos" : "top",
        "text_duration" : 3,
        "show_text": True,
        "speed" : 3,
    },
    {
        "time" : (9,24),
    },
    {
        "time" : (9,35),
        "text" : "makefile ORing",
    },
    {
        "time" : (10,0),
        "text" : "append steps",
    },
    {
        "time" : (11,20),
        "text" : "cover LED data",
    },
    {
        "time" : (12,00),
        "text" : "write signal is now toggling",
    },
    {
        "time" : (12,23),
        "text" : "2 LEDs",
    },
    {
        "time" : (12,41),
        "text" : "AABBCC data is seen",
        "text_duration" : 3,
    },
    {
        "time" : (12,45),
        "comp" : [ "background", "webcam" ],
        "clip_size" : { 'webcam' : (800,600), 'background' : (1280,800) },
        "clip_pos" : { 'webcam' : ((1280 - 800)/2, (800-600)/2), 'background': (0,0) },
        "text" : "summary",
    },
    {
        "time" : (13,8),
        "comp" : [ "background", "webcam" ],
        "clip_size" : { 'webcam' : (800,600), 'background' : (1280,800) },
        "clip_pos" : { 'webcam' : ((1280 - 800)/2, (800-600)/2), 'background': (0,0) },
        "text" : "COMMENTS!!!",
        "show_text": True,
    },
    {
        "time" : (13,15),
        "comp" : None,
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
