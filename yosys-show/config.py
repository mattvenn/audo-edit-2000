config = {
    'outfile': 'show.mp4',
    'files': 
    {
            'webcam' :
            { 
                'type' : 'video',
                'file' : 'yosys-show-webcam.mkv', #  1280 x 800
                'start': 0,
                'audio': True,
            },
            'screen' :
            {
                'type' : 'video',
                'file' : 'yosys-show-screen.mkv', # 800 x 600
                'start': 1.5,
                'audio': False,
            },
            'background'   :
            {
                'file' : 'ice40-die.jpeg',
                'type' : 'image',
            },
    },
    'sequence_defaults' :
    {
        "comp" : [ 'screen', 'webcam' ],
        'clip_size' : { 'webcam' : 400, 'screen' : 1280, 'background' : 1280 }, # desired width of video clips
        'clip_pos' : { 'webcam' : (1280 - 400, 0), 'screen' : (0,0), 'background' : (0,0) },
        "text" : None,
        "text_vpos" : "bottom",
        "title_duration" : 5, # how long to show titles
        "title_fade_duration" : 0.4, # how long to fade in and out the titles
        "duration" : 0, # duration of the final clip
        "speed": 1,
    },
    ##########################################################
    'sequence' : [
    {
        "time" : (0,22),
        "comp" : [ "background", "webcam" ],
        "clip_size" : { 'webcam' : 800, 'background' : 1280 },
        "clip_pos" : { 'webcam' : ((1280 - 800)/2, (800-600)/2), 'background': (0,0) },
        "text" : "yosys show",
    },
    {
        "time" : (0,38),
        "text" : "github.com/mattvenn/icestick-multisegment",
    },
    {
        "time" : (1,3),
        "text" : "multisegment LED",
    },
    {
        "time" : (1,22),
        "text" : "make and prog",
    },
    {
        "time" : (1,25),
        "text" : "exciting demo!",
        "comp" : [ "background", "webcam" ],
        "clip_size" : { 'webcam' : 800, 'background' : 1280 },
        "clip_pos" : { 'webcam' : ((1280 - 800)/2, (800-600)/2), 'background': (0,0) },
    },
    {
        "time" : (1,33),
    },
    {
        "time" : (1,38),
        "text" : "yosys show",
    },
    {
        "time" : (1,58),
        "text" : "help show",
    },
    {
        "time" : (2,4),
        "text" : "colors & width",
    },
    {
        "time" : (2,18),
        "comp" : [ "screen" ],
        "text" : "output",
    },
    {
        "time" : (3,9),
        "text" : "signal vectors",
    },
    {
        "time" : (3,40),
        "text" : "summary",
    },
    {
        "time" : (3,50),
        "text" : "yosys appnote 011",
    },
    {
        "time" : (4,14),
        "comp" : None,
    },
    ]
}
