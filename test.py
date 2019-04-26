from moviepy.editor import *
TITLE_DURATION = 5
webcam_w = 300
screen = VideoFileClip("cover-screen.mkv").without_audio()
screen = screen.without_audio()

webcam_x = screen.w - webcam_w
webcam = VideoFileClip("cover-webcam.mkv").resize(width=webcam_w).set_pos((webcam_x,0))
webcam = webcam.without_audio()

shot_list = []
from sequence import sequence, ShotType

for shot_num in range(len(sequence)):
    shot = sequence[shot_num]
    if shot['type'] == ShotType.end:
        break
        
    shot_start = sequence[shot_num]['time']
    shot_end   = sequence[shot_num+1]['time']

    screen_clip = screen.subclip(shot_start, shot_end)
    webcam_clip = webcam.subclip(shot_start, shot_end)

    if shot['type'] == ShotType.title:
        print("making title: %s" % shot["text"])
        title_clip = ( TextClip(shot["text"], fontsize=70, color='white', bg_color='black', font='Arial-Bold')
                     .set_position("bottom", "center")
                     .set_duration(TITLE_DURATION))
    
        shot_list.append( CompositeVideoClip([screen_clip, webcam_clip, title_clip]))

    elif shot['type'] == ShotType.speedup:
        print("speeding up section %d" % shot_num)
        # remove audio from sped up parts
        shot_list.append( CompositeVideoClip([screen_clip, webcam_clip.without_audio()]).fx(vfx.speedx, shot['speed']))

    elif shot['type'] == ShotType.cut:
        pass

    else:
        pass

import time
start_time = time.time()
result = concatenate_videoclips(shot_list)
result.write_videofile("rendered.mp4",fps=20)
print("finished rendering in %d seconds" % time.time() - start_time())
