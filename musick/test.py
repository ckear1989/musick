
import os

from pydub import AudioSegment
from pydub.playback import play


empty = AudioSegment.silent(100)
song = AudioSegment.from_mp3('../ext/source.mp3')
print(dir(song))
print(song.duration_seconds)
beat0 = song[:2000]
beat0 = beat0.strip_silence()
beat0 = beat0[400:750].fade_out(10)
beat0 = beat0 + empty
print(beat0.duration_seconds)
play(beat0)
bar = beat0 * 4
print(bar.duration_seconds)
play(bar)
beat1 = song[50000:52000].strip_silence()
beat1 = beat1[400:750].fade_out(10)
beat1 = beat1 + empty
beat1 = AudioSegment.silent(beat1.duration_seconds/1000) + beat1
print(beat1.duration_seconds)
bar1 = beat1 * 2
print(bar1.duration_seconds)
play(bar1)
bar = bar.overlay(bar1, loop=True)
play(bar)

new_song = bar * 10
new_song = new_song.fade_in(100).fade_out(100)
play(new_song)

new_song.export('../ext/mashup.mp3', format='mp3')

