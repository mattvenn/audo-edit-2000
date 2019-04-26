stem = '%s : https://youtu.be/n_N-JL914UE?t=%d'
from sequence import sequence, ShotType
def to_seconds(timing):
    return timing[0] * 60 + timing[1]

# these shot times are based off the original video, so need to be adjusted for cut , speed and offset
for shot_num in range(len(sequence)):
    shot = sequence[shot_num]
    shot_start = sequence[shot_num]['time']
    if shot['type'] == ShotType.title:
        print(stem % (shot['text'], to_seconds(shot_start)))
