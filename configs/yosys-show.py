config = {
    'outfile': 'yosys-show/show.mp4',
    'files': 
    {
            'webcam' :
            { 
                'type' : 'video',
                'file' : 'yosys-show/yosys-show-webcam.mkv', # 800 x 600
                'start': 0,
                'audio': 'yosys-show/yosys-show-webcam.wav', 
                'audio_offset' : 0.25,  # 0.25s out - vlc adjusted -0.25s (hastened)
            },
            'screen' :
            {
                'type' : 'video',
                'file' : 'yosys-show/yosys-show-screen.mkv', # 1280 x 800
                'start': 2.25, # was 1.5. vlc adjusted -0.75s (hastened)
                'audio': False,
            },
            'intro' :
            {
                'type' : 'video',
                'file' : 'yosys-show/symbiotic-intro.mp4', # 1280 x 800
                'start': 0,
                'audio': False,
            },
            'background'   :
            {
                'file' : 'yosys-show/ice40-die.jpeg',
                'type' : 'image',
            },
    },
    'sequence_defaults' :
    {
        "comp" : [ 'screen', 'webcam' ],
        'clip_size' : { 'intro' : (1280,800), 'webcam' : (400,300), 'screen' : (1280,800), 'background' : (1280,800) }, # desired width of video clips
        'clip_pos' : { 'intro' : (0,30), 'webcam' : (1280 - 400, 0), 'screen' : (0,0), 'background' : (0,0) },
        "text" : None,
        "text_vpos" : "top",
        "text_size" : 50,
        "text_duration" : 5, # how long to show text
        "text_fade_duration" : 0.4, # how long to fade in and out the text
        "duration" : 0, # duration of the final clip
        "speed": 1,
        "show_text" : False,
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
        "time" : (0,22),
        "comp" : [ "background", "webcam" ],
        "clip_size" : { 'webcam' : (800,600), 'background' : (1280,800) },
        "clip_pos" : { 'webcam' : ((1280 - 800)/2, (800-600)/2), 'background': (0,0) },
        "text" : "yosys show",
        "show_text": True,
    },
    {
        "time" : (0,38),
        "text_size" : 50,
        "text" : "github.com/mattvenn/icestick-multisegment",
        "show_text": True,
    },
    {
        "time" : (1,3),
        "text" : "multisegment LED",
    },
    {
        "time" : (1,21),
        "text" : "make and prog",
    },
    {
        "time" : (1,25),
        "text" : "exciting demo!",
        "show_text": True,
        "comp" : [ "background", "webcam" ],
        "clip_size" : { 'webcam' : (800,600), 'background' : (1280,800) },
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
        "text" : "output",
    },
    {
        "time" : (3,9),
        "text" : "signal vectors",
        "show_text": True,
    },
    {
        "time" : (3,40),
        "comp" : [ "background", "webcam" ],
        "clip_size" : { 'webcam' : (800,600), 'background' : (1280,800) },
        "clip_pos" : { 'webcam' : ((1280 - 800)/2, (800-600)/2), 'background': (0,0) },
        "text" : "summary",
    },
    {
        "time" : (3,50),
        "text" : "appnote: http://bit.ly/yosys_appnote_011",
        "show_text": True,
    },
    {
        "time" : (4,14),
        "comp" : None,
    },
    ]
}
