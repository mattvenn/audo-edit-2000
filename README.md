# auto edit 2000

* simple program using [moviepy](https://zulko.github.io/moviepy/) to composite and do basic editing on a pair of recorded videos.
* use the ffmpeg scripts in recording-tools to record webcam (+audio) and screen cap.
* create a [sequence](sequence.py) of titles, cuts, and speedups.
* render to mp4 video

# types of edits I want

I'm building this tool to make it easier to create and publish howto style videos. I'm recording webcam and screen caps and then want something else to do all the editing. The kinds of things I want to make easy:

* create titles - done
* skip sections - done
* speed up sections - done
* have webcam composited in top-right corner of screen cap - done (default)
* fullscreen webcam for some sections - todo
* generate a youtube compatible TOC - todo
* full screen titles - todo

# todo

* can't preview the transitions because of errors with moviepy. get errors very similar to this: https://github.com/Zulko/moviepy/issues/863, if audio is removed, preview works
* start the recordings together to avoid having to correct in the sequencer
* video links don't work for TOC
* command line args to choose videos/config to use

# project notes

## Thu 25 Apr 18:35:03 CEST 2019

check to see if recordmydesktop can do the compression on the fly like ffmpeg
next time check cpu usage
seemed to be ok though

## Fri 26 Apr 16:44:05 CEST 2019

yes, use onthefly encoding - 10 seems ok.
problem now is the webcam recording is very poor unsynchronised audio with lots of dropouts
tried adding thread_queue_size option, seems to improve things

video sync how to do it?

gave up on recordmydesktop, too long a wait after recording without onthefly encoding, but too variable a framerate with onthefly encoding. using ffmpeg instead.

