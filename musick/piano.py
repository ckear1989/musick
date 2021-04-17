
from pydub import AudioSegment
from pydub.playback import play

from drum import DrumBar

class Piano(DrumBar):
    def __init__(self, sample, bpm, beats_per_bar):
        super().__init__(sample, bpm, beats_per_bar)

if __name__=='__main__':
    piano_dir = '../ext/piano/musicradar-broken-piano-samples/'
    sample0 = piano_dir + 'Raw/Strings/Discordant 01.wav'
    sample0 = AudioSegment.from_file(sample0)
    play(sample0)
    sample0_bar = Piano(sample0, 200, 4)
    play(sample0_bar.bar)

