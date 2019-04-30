#!/usr/bin/env python
import sys
import argparse
import time
from moviepy.editor import *
import logging
import numpy as np

# utilities to get defaults for missing keys in the config
def get_clip_property(key, shot, clip_name):
    return shot.get(key, config['sequence_defaults'][key])[clip_name]

def get_shot_property(key, shot):
    return shot.get(key, config['sequence_defaults'][key])

# utility for lining up the 2 videos
def offset(timing, offset):
    minute = timing[0]
    second = timing[1]
    seconds = minute * 60 + second
    seconds -= offset
    minute = int(seconds / 60)
    second = seconds - minute * 60
    return (minute, second)

# return seconds
def get_shot_duration(start, end):
    return (end[0] * 60 + end[1]) - (start[0] * 60 + start[1])

def create_sequence():
    sequence = config['sequence']
    shot_list = []

    for shot_num, shot in enumerate(sequence[0:-1]): # last item in sequence is 'end' placeholder
        logging.info("sequence %02d/%02d" % (shot_num+1, len(sequence)-1))
        
        if args.max_shot is not None:
            if shot_num == args.max_shot - 1:
                logging.info("ending early due to --max-shot")
                break

        comp = get_shot_property('comp', shot)
        if comp is None:
            shot['shot_duration'] = 0
            logging.info("skipping shot %d" % (shot_num+1))
            continue
            
        # do this to avoid repetition of times in the config file
        shot_start = sequence[shot_num]['time']
        shot_end   = sequence[shot_num+1]['time']

        shot_speed = get_shot_property('speed', shot)
        shot_text  = get_shot_property('text', shot)
        shot_title_fade_duration  = get_shot_property('title_fade_duration', shot)
        shot_text_vpos = get_shot_property('text_vpos', shot)

        shot['clips'] = []
        # get the subclips and configure them
        for clip_name in comp:
            clip_type = config['files'][clip_name]['type']
            if clip_type == 'video':
                clip_offset = config['files'][clip_name]['start']
                offset_start = offset(shot_start, clip_offset)
                offset_end   = offset(shot_end,   clip_offset)
                clip = config['files'][clip_name]['clip'].subclip(offset_start, offset_end)
                logging.debug("clip %s start/end %s %s adj start/end %s %s" % 
                             (clip_name, shot_start, shot_end, offset_start, offset_end))
                
            elif clip_type == 'image':
                clip = config['files'][clip_name]['clip'].set_duration(get_shot_duration(shot_start, shot_end))

            # return defaults if not set
            clip_size  = get_clip_property('clip_size', shot, clip_name)
            clip_pos   = get_clip_property('clip_pos' , shot, clip_name)

            logging.info("clip %s set size = %d and position = %s" % (clip_name, clip_size, clip_pos))

            # set size and pos here
            clip = clip.resize(width=clip_size).set_pos(clip_pos)

            # audio
            if shot_speed != 1:
                logging.info("clip %s speed = %d" % (clip_name, shot_speed))
                clip = clip.without_audio().fx(vfx.speedx, shot_speed) 

            # store the clip in the config
            shot['clips'].append(clip)

        # make a title?
        if shot_text is not None:
            logging.info("making title: %s" % shot_text)
            title_clip = (TextClip(shot_text, fontsize=70, color='white', bg_color='gray', font='D-Din')
                         .set_position(shot_text_vpos, "center")
                         .set_duration(get_shot_property('title_duration', shot)))

            # fade it in and out?
            if shot_title_fade_duration != 0:
                arr = np.ones((title_clip.h,title_clip.w))
                mask = ImageClip(arr, ismask=True, duration=title_clip.duration)
                mask = mask.fx(vfx.fadein, shot_title_fade_duration, initial_color=0). \
                            fx(vfx.fadeout, shot_title_fade_duration, final_color=0)
                title_clip = title_clip.set_mask(mask)

            # put the title in the list of clips to render
            shot['clips'].append(title_clip)

        # composite the clips and store
        shot['clip'] = CompositeVideoClip(shot['clips'])
        shot['duration'] = shot['clip'].duration
    
# useful functions for previewing the clips and transitions
def preview_transition(index, preview_length=10):
    clip1 = config['sequence'][index]['clip']
    clip2 = config['sequence'][index+1]['clip']
    concatenate_videoclips([clip1, clip2]).subclip(
                clip1.duration - preview_length/2, clip1.duration + preview_length/2).preview()

def preview(index):
    config['sequence'][index]['clip'].preview()

def sec_to_min(seconds):
    minutes = int(seconds / 60)
    seconds = seconds - minutes * 60
    return "%02d:%02d" % (minutes, seconds)

def print_sections():
    run_time = 0
    for shot_num, shot in enumerate(config['sequence'][0:-1]):
        shot_speed = get_shot_property('speed', shot)
        shot_text  = get_shot_property('text', shot)
        shot_duration  = get_shot_property('duration', shot)
        logging.info("%02d : runtime %s length %s text: %s speed: %s" % (shot_num+1, sec_to_min(run_time), sec_to_min(shot_duration), shot_text, shot_speed))
        run_time += shot_duration
    logging.info("total duration = %s" % sec_to_min(run_time))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="simple automated video editing")
    parser.add_argument('--config', required=True, help="directory that contains the config.py configuration file")
    parser.add_argument('--max-shot', type=int, help="process up to this number of shots in the sequence")
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

    # load the clips
    for name, file_conf in config['files'].items():
        if file_conf['type'] == 'video':
            logging.info("opening video for file %s" % name)
            clip = VideoFileClip(args.config + file_conf['file'])
            if not file_conf['audio']:
                logging.info("removing audio for file %s" % name)
                clip = clip.without_audio()
        elif file_conf['type'] == 'image':
            logging.info("opening image for file %s" % name)
            clip = ImageClip(args.config + file_conf['file'])
        else:
            logger.warning("no such file type %s" % file_conf['type'])
            exit(1)
        file_conf['clip'] = clip

    # using the config, create all the clips and store in config['sequence'][index]['clip']
    create_sequence()

    # get all the clips and join them together
    clips = []
    for shot in config['sequence']:
        if 'clip' in shot:
            clips.append(shot['clip'])

    import ipdb; ipdb.set_trace()
    final = concatenate_videoclips(clips)

    logging.info("rendering to %s" % config['outfile'])
    start_time = time.time()
    final.write_videofile(config['outfile'], fps=20, threads=4) # audio_fps=44100,codec = 'libx264'
    logging.info("finished rendering in %s" % sec_to_min(time.time() - start_time))
