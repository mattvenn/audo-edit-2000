import argparse
import time
from moviepy.editor import *
import logging

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

def create_sequence():
    sequence = config['sequence']
    shot_list = []

    for shot_num, shot in enumerate(sequence):
        if shot_num == len(sequence)-1: # last shot is a placeholder
            logging.info("last shot")
            break

        logging.info("sequence %02d/%02d" % (shot_num, len(sequence)))
        
        comp = get_shot_property('comp', shot)
        if comp is None:
            logging.info("skipping shot %d" % shot_num)
            continue
            
        # do this to avoid repetition of times in the config file
        shot_start = sequence[shot_num]['time']
        shot_end   = sequence[shot_num+1]['time']

        shot_speed = get_shot_property('speed', shot)
        shot_text  = get_shot_property('text', shot)

        shot['clips'] = []
        # get the subclips and configure them
        for clip_name in comp:
            clip_offset = config['files'][clip_name]['start']
            offset_start = offset(shot_start, clip_offset)
            offset_end   = offset(shot_end,   clip_offset)
            clip = config['files'][clip_name]['clip'].subclip(offset_start, offset_end)
            logging.debug("clip %s start/end %s %s adj start/end %s %s" % 
                             (clip_name, shot_start, shot_end, offset_start, offset_end))

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
            title_clip = (TextClip(shot_text, fontsize=70, color='white', bg_color='black', font='Arial-Bold')
                         .set_position("bottom", "center")
                         .set_duration(get_shot_property('title_duration', shot)))

            # put the title in the list of clips to render
            shot['clips'].append(title_clip)

        # composite the clips and store
        shot['clip'] = CompositeVideoClip(shot['clips'])
    
def preview_transition(index, preview_length=10):
    clip1 = config['sequence'][index]['clip']
    clip2 = config['sequence'][index+1]['clip']
    concatenate_videoclips([clip1, clip2]).subclip(
                clip1.duration - preview_length/2, clip1.duration + preview_length/2).preview()

def preview(index):
    config['sequence'][index]['clip'].preview()

def print_sections():
    for shot_num, shot in enumerate(config['sequence']):
        shot_speed = get_shot_property('speed', shot)
        shot_text  = get_shot_property('text', shot)
        shot_comp  = get_shot_property('comp', shot)
        logging.info("%02d : %s %s %s" % (shot_num, shot_text, shot_speed, shot_comp ))

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

    # load the clips
    for name, file_conf in config['files'].items():
        logging.info("opening video for file %s" % name)
        clip = VideoFileClip(args.config + file_conf['file'])
        if not file_conf['audio']:
            logging.info("removing audio for file %s" % name)
            clip = clip.without_audio()
        file_conf['clip'] = clip

    # using the config, create all the clips and store in config['sequence'][index]['clip']
    create_sequence()

    # get all the clips and join them together
    clips = []
    for shot in config['sequence']:
        if 'clip' in shot:
            clips.append(shot['clip'])
    final = concatenate_videoclips(clips).subclip(20,24)

    import ipdb; ipdb.set_trace()

    logging.info("rendering to %s" % config['outfile'])
    start_time = time.time()
    final.write_videofile(config['outfile'], fps=20)
    logging.info("finished rendering in %d seconds" % (time.time() - start_time))
