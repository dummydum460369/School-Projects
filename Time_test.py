from time import *

x = ctime()
print(x)
bpm = float(input('enter Bpm:'))
bps = bpm / 60
metronome = 1 / bps
count = 0
timing_beat = float(input('Enter beats per bar:'))
while True:
    y = time()
    while time() < y + metronome:
        pass
    if count % timing_beat == 0:
        print('\nTICK', end=' ')
        count += 1
    else:
        print('tick', end=' ')
        count += 1
