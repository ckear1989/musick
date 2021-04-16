
import random
import numpy as np

from pydub import AudioSegment
from pydub.playback import play

random.seed(123)

empty = AudioSegment.silent(100)
song = AudioSegment.from_mp3('../ext/source.mp3')
song_ms = int(song.duration_seconds * 1000)
print(dir(song))
print(song.duration_seconds)
beat0 = song[:2000]
beat0 = beat0.strip_silence()
beat0 = beat0[400:750].fade_out(10)
beat0 = beat0 + empty
print(beat0.duration_seconds)
# play(beat0)
bar = beat0 * 4
print(bar.duration_seconds)
# play(bar)
beat1 = song[50000:52000].strip_silence()
beat1 = beat1[400:750].fade_out(10)
beat1 = beat1 + empty
beat1 = AudioSegment.silent(beat1.duration_seconds/1000) + beat1
print(beat1.duration_seconds)
bar1 = beat1 * 2
print(bar1.duration_seconds)
# play(bar1)
bar = bar.overlay(bar1, loop=True)
# play(bar)

new_song = bar * 10
new_song = new_song.fade_in(100).fade_out(100)
# play(new_song)

new_song.export('../ext/mashup.mp3', format='mp3')

note0 = beat0[-200:-198]
note0 = note0 * 100
print(note0.duration_seconds)
play(note0)
note1 = beat0[-300:-298]
note1 = note1 * 100
print(note1.duration_seconds)
play(note1)
tune = note0 + note1 + empty + note1 + note0
play(tune)

new_song = (new_song - 3).overlay(tune, loop=True)
# play(new_song)

song_ms_s = [i for i in range(song_ms)]
print(song_ms_s[:10])
print(song_ms_s[-10:])
class Note():
    def __init__(self, length=random.sample([1, 2, 3, 4, 5], 1)[0], repeat=int(round(np.random.normal(100, 20)))):
        self.length = length
        self.repeat = repeat
        self.note = song[start_time:(start_time+random.sample([1, 2, 3, 4, 5], 1)[0])] * int(round(np.random.normal(100, 20)))

for i in range(20):
  start_time = random.sample(song_ms_s, 1)[0]
  print(start_time)
  sample = Note().note
  print(sample.duration_seconds)
  play(sample)
  tune += sample + AudioSegment.silent(np.random.normal(200, 40))

play(tune)
new_song = new_song.overlay(tune, loop=True)
play(new_song)

