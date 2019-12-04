echo $1
device=2,0
#ffmpeg -f alsa -i hw:3 -f v4l2 -framerate 20 -video_size 800x600 -input_format mjpeg -i /dev/video0 -preset faster $1.mkv
ffmpeg -nostdin -f alsa -thread_queue_size 2048 -sample_rate 44100 -i hw:$device \
-f v4l2 -thread_queue_size 2048 -framerate 20 -video_size 800x600 -input_format mjpeg -i /dev/video0  $1.mkv > $1.log 2>&1
