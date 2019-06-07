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
* be able to have seperate short videos at start/end etc - done
* be able to change audio sync - seems off on yosys-show vid - done
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

# Mon  6 May 20:00:51 CEST 2019

tried with docker. yosys show took 2:19
use digital-ocean-api and moviepy_setup.sh to get docker installed and latest docker setup
scp -r yosys-show root@xxx:~/

on new machine:

docker run -v ~/yosys-show:/yosys-show -ti mattvenn/moviepy:install_3 /bin/bash

then cd /home/moviepy/auto-edit-2000
git pull
ln -s /yosys-show
python render.py --config configs/yosys-show.py

02:33 - c4 instance,  4 threads
02:23 - c4 instance, 16 threads

# Fri 10 May 17:29:50 CEST 2019

something about the new yosys show config (intro animation or sizing?) has increased render time to 7 minutes

docker updating:
* make changes
* exit
* docker commit <id> -m "commit message" mattvenn/moviepy:<newtag>
* docker login
* docker push mattvenn/moviepy:<newtag>

new commands for rendering video from droplet:

# show
scp -r matt@mattvenn.net:~/symbiotic-videos/yosys-show .
docker run -v ~/yosys-show:/auto-edit-2000/yosys-show -ti mattvenn/moviepy:install_4 /bin/bash -c "cd auto-edit-2000; pwd; git pull; ./render.py --config configs/yosys-show.py"

# cover
scp -r matt@mattvenn.net:~/symbiotic-videos/cover .
docker run -v ~/cover:/auto-edit-2000/cover -ti mattvenn/moviepy:install_4 /bin/bash -c "cd auto-edit-2000; pwd; git pull; ./render.py --config configs/cover.py"

# axi-lite formal
docker run -v ~/axi-lite-formal:/auto-edit-2000/axi-lite-formal -ti mattvenn/moviepy:install_4 /bin/bash -c "cd auto-edit-2000; pwd; git pull; ./render.py --config axi-lite-formal/config.py"

# Mon 20 May 19:26:24 CEST 2019

performance investigation
yosys show

aa25ee4f634da8314bd83a07fa2b50d1552be32f : 2:16
ae4291f875cd893aaea76f298e2e06a7b3567293 : 2:23
6a95ed944ff027b4922a1aa0d6b978b5353174f0 : ~ 8
0a51df5a0c7a8447d87935f06ecd893ab2e1b648 : ~ 8 <--- commit that wrecked timing - added "compose" to the concatenate method
ae4291f875cd893aaea76f298e2e06a7b3567293 : ~ 2

axi-lite-formal 61:02 (with compose)
axi-lite-formal 21:03 (without compose)
cover: 6:57 (without compose)

## git lfs

sudo apt-get install git-lfs
git-lfs clone https://github.com/mattvenn/axi-lite-formal-video
docker run -v ~/axi-lite-formal-video:/auto-edit-2000/axi-lite-formal-video -ti mattvenn/moviepy:install_4 /bin/bash -c "cd auto-edit-2000; pwd; git pull; ./render.py --config axi-lite-formal-video/config.py"

## generic CLI

video=yosys-show-video
git clone https://github.com/mattvenn/$video
docker run -v ~/$video:/auto-edit-2000/$video -ti mattvenn/moviepy:install_4 /bin/bash -c "cd auto-edit-2000; pwd; git pull; ./render.py --dir $video"
