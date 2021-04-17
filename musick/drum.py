
from pydub import AudioSegment
from pydub.playback import play

class DrumBar():
    def __init__(self, sample, bpm, beats_per_bar):
        seconds_per_beat = 60.0 / float(bpm)
        duration = seconds_per_beat * beats_per_bar * 1000
        out = AudioSegment.silent(duration)
        interval = duration / (beats_per_bar)
        interval = AudioSegment.silent(interval)
        for x in range(beats_per_bar):
            out = out.overlay(interval * x + sample)
        self.bar = out
        

if __name__ == '__main__':
    drum_dir = '../ext/drum/musicradar-drum-samples/'
    sample0_f = drum_dir + 'Assorted_Hits/Cymbals/CYCdh_Crash-01.wav'
    sample0 = AudioSegment.from_file(sample0_f)
    # play(sample0)
    sample0 = sample0[:2000].fade_out(500).fade_out(200)
    play(sample0)
    sample0.export('../ext/drum/cymbal0.wav', format='wav')
    sample_bar0 = DrumBar(sample0, 100, 4)
    play(sample_bar0.bar)
    sample_bar1 = DrumBar(sample0, 150, 4)
    play(sample_bar1.bar)
    play(DrumBar(sample0, 200, 4).bar * 4)

