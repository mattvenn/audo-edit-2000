echo $1
#recordmydesktop --on-the-fly-encoding --no-sound --fps 20 --width 2560 --height 1700 -x0 -y0 --v_quality=20 -o $1.ogv
ffmpeg -nostdin -video_size 2560x1600 -framerate 20 -f x11grab -i :0.0+0,0 -vf scale=1280:800 $1.mkv 
