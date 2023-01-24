from midiutil.MidiFile import MIDIFile

file_name = "results/5_DGAFDGAFDGAFDGAF.txt"
file_to_convert = open(file_name, 'r')

pitches = {
    'C': 48,
    'C#': 49,
    'Db': 49,
    'D': 50,
    'D#': 51,
    'Eb': 51,
    'E': 52,
    'F': 53,
    'F#': 54,
    'Gb': 54,
    'G': 55,
    'G#': 56,
    'Ab': 56,
    'A': 57,
    'A#': 58,
    'Bb': 58,
    'B': 59
}

time = 0
track = 0
track_name = "test5"
bpm = 120

mf = MIDIFile(1)

mf.addTrackName(track=track, time=time, trackName=track_name)
mf.addTempo(track=track, time=time, tempo=bpm)

for line in file_to_convert:
    pitch = pitches[line.strip()]
    duration = 1
    mf.addNote(track=track, channel=0, pitch=pitch, time=time, duration=duration, volume=100)
    time += duration

with open(f'output/{track_name}.mid', 'wb') as output_file:
    mf.writeFile(output_file)

print(f'Created midi file: {track_name}.mid')