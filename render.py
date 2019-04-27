import argparse
from moviepy.editor import *
import logging

from enum import Enum
class ShotType(Enum):
    webcam = 1
    screen_webcam = 2
    screen = 3
    speedup = 4
    cut = 5
    end = 6

# utility for lining up the 2 videos
def offset(timing, offset):
    minute = timing[0]
    second = timing[1]
    seconds = minute * 60 + second
    seconds -= offset
    minute = int(seconds / 60)
    second = seconds - minute * 60
    return (minute, second)

def create_sequence(config):
    sequence = config['sequence']
    shot_list = []

    for shot_num in range(len(sequence)):
        shot = sequence[shot_num]
        if shot['type'] == ShotType.end.name:
            break
            
        shot_start = sequence[shot_num]['time']
        shot_end   = sequence[shot_num+1]['time']

        screen_clip = screen.subclip(offset(shot_start, config['webcam_t_offset']), 
                                        offset(shot_end, config['webcam_t_offset']))

        webcam_clip = webcam.subclip(shot_start, shot_end)

        # make a title?
        title_clip = None
        if 'text' in shot:
            logging.info("making title: %s" % shot["text"])
            title_clip = ( TextClip(shot["text"], fontsize=70, color='white', bg_color='black', font='Arial-Bold')
                         .set_position("bottom", "center")
                         .set_duration(config['title_duration']))

        # different shot types
        if shot['type'] == ShotType.cut.name:
            logging.info("skipping shot %d" % shot_num)
            pass

        elif shot['type'] == ShotType.webcam.name:
            logging.info("%02d: webcam priority" % shot_num)
            if title_clip is not None:
                webcam_clip = webcam_clip.set_pos("center")
                shot_list.append(CompositeVideoClip([screen_clip, webcam_clip, title_clip]))
            else:
                shot_list.append(webcam_clip)

        elif shot['type'] == ShotType.screen_webcam.name:
            logging.info("%02d: screen + webcam" % shot_num)
            webcam_x = screen.w - config['webcam_w']
            webcam_clip = webcam_clip.resize(width=config['webcam_w']).set_pos((webcam_x,0))

            if title_clip is not None:
                clips = [screen_clip, webcam_clip, title_clip]
            else:
                clips = [screen_clip, webcam_clip]

            comp_clip = CompositeVideoClip(clips)

            if "speed" in shot:
                logging.info("%02d: speedup x %d" % (shot_num, shot['speed'])
                # remove audio from sped up parts
                comp_clip = comp_clip.without_audio().fx(vfx.speedx, shot['speed'])

            shot_list.append(comp_clip)

        else:
            logging.warning("unknown shot type: %s" % shot['type'])
            exit(1)
    
    return shot_list

def preview_transition(shot_list, index, preview_length=10):
    concatenate_videoclips([shot_list[index],shot_list[index+1]]).subclip(
                shot_list[index].duration - preview_length/2, shot_list[index].duration + preview_length/2).preview()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="simple automated video editing")
    parser.add_argument('--config', required=True, help="directory that contains the config.py configuration file")
    parser.add_argument("-v", "--verbose", dest="verbose_count",
                            action="count", default=1,
                            help="increases log verbosity for each occurence.")

    args = parser.parse_args()
    log_level = max(3 - args.verbose_count, 0) * 10
    logging.basicConfig(level=log_level, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    sys.path.append(args.config)
    try:
        from config import config
    except ImportError:
        exit("no sequence.py found in %s" % args.config)

    screen = VideoFileClip(args.config + config['screen']).without_audio()

    webcam = VideoFileClip(args.config + config['webcam'])

    shot_list = create_sequence(config)

    import ipdb; ipdb.set_trace()


    exit(0)
    import time
    logging.info("rendering")
    start_time = time.time()
    result = concatenate_videoclips(shot_list)
    result.write_videofile("rendered.mp4",fps=20)
    logging.info("finished rendering in %d seconds" % (time.time() - start_time))
