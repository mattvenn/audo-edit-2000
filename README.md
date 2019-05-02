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
* fullscreen webcam for some sections - done
* insert images full screen - done
* fade titles or have some nicer transition - done
* position of titles - done
* generate a youtube compatible TOC - done
* full screen titles - todo
* put font/threads into config - todo

# requirements

* apt-get install imagemagick
* pip install moviepy
* install D-Din font: https://medium.com/source-words/how-to-manually-install-update-and-uninstall-fonts-on-linux-a8d09a3853b0
* imagemagick policy: https://github.com/Zulko/moviepy/issues/693

# todo

* can't preview the transitions because of errors with moviepy. get errors very similar to this: https://github.com/Zulko/moviepy/issues/863, if audio is removed, preview works
* start the recordings together to avoid having to correct in the sequencer
* video links don't work for TOC
* command line args to choose videos/config to use
* record webcam tool seems to make audio sync out by about 0.1 second

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

# Tue 30 Apr 19:42:14 CEST 2019

investigating why moviepy corrupts some video files with show/load/write/preview. only a problem on the screen capture.

but then doing another capture with same record tool and can preview fine.
does work on my old laptop at home. versions?
workshop pc: moviepy version '0.2.3.2', ffmpeg 2.8.15,      139c49acce8f7465d04fa671df6d02  cover/cover-screen.mkv
laptop:      moviepy version '1.0.0',   ffmpeg 3.4.4-0,     0a139c49acce8f7465d04fa671df6d03

# Thu  2 May 11:21:04 CEST 2019

tried with digitalocean 16 core (set threads to 16 ffmpeg):
had to install font and change name to D\-Din
didn't seem to use many cores, maybe 2. 13% reported by digital ocean metrics
auto installed some special kind of ffmpeg: ~/.imageio/ffmpeg/ffmpeg-linux64-v3.3.1 -version
ffmpeg version N-86111-ga441aa90e8-static http://johnvansickle.com/ffmpeg/  Copyright (c) 2000-2017 the FFmpeg developers

* yosys show took 2:29.
* cover took 7:22

videos were undistorted!
