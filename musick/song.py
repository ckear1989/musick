
from pydub import AudioSegment
from pydub.playback import play

from drum import DrumBar
from piano import Piano

class Song():
    def __init__(
        self,
        drum,
        piano,
        bpm,
        bpb,
        duration,
        drum_offset=0,
        piano_offset=0
        ):
        self.drum = DrumBar(drum, bpm, bpb).bar + drum_offset
        self.piano = Piano(piano, bpm, bpb).bar + piano_offset
        self.bar = self.drum.overlay(self.piano)
        bars = round(float(duration) / float(self.bar.duration_seconds))
        self.song = self.bar * bars

if __name__ == '__main__':
    drum_dir = '../ext/drum/musicradar-drum-samples/'
    drum0 = drum_dir + 'Assorted_Hits/Cymbals/CYCdh_Crash-01.wav'
    drum0 = AudioSegment.from_file(drum0)
    drum0 = drum0[:2000].fade_out(500).fade_out(200)
    piano_dir = '../ext/piano/musicradar-broken-piano-samples/'
    piano0 = piano_dir + 'Raw/Strings/Discordant 01.wav'
    piano1 = piano_dir + 'Raw/Strings/Strings 01.wav'
    piano2 = piano_dir + 'Raw/Strings/Single 01.wav'
    piano0 = AudioSegment.from_file(piano0)
    piano1 = AudioSegment.from_file(piano1)
    piano2 = AudioSegment.from_file(piano2)
    song0 = Song(drum0, piano0, 150, 4, 15, drum_offset=-10)
    song1 = Song(drum0, piano1, 150, 4, 15, drum_offset=-10)
    song2 = Song(drum0, piano2, 150, 4, 10, drum_offset=-10, piano_offset=10)
    song3 = Song(drum0, piano2, 150, 4, 20, drum_offset=-10, piano_offset=20)
    play(song0.song + song1.song + song2.song + song3.song)
