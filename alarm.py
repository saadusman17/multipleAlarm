import time

import pyaudio
import wave
import sys


def playsound(sound_file):

    CHUNK = 1024

    wf = wave.open(sound_file, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()


no_of_alarms = 16

try:
    input = raw_input
except NameError:
    pass

key_input = input("press enter to start")
print "counting for 1 minute"

gap = 60
activity_duration = 270

time.sleep(gap)
playsound('dong.wav')


for i in range(0, no_of_alarms):
    print "counting for 4.5 minutes"
    time.sleep(activity_duration)
    playsound('ding.wav')
    print "counting for 1 minute break"
    time.sleep(gap)
    playsound('dong.wav')
