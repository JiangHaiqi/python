#-*-coding: utf-8 -*-
#Script Name:   wave_play.py
#Auther:        Haiqi Jiang
#Created:       15th July
#Last Modified:
#Version:
"""
This python script is aimed at playing the Music file(.wav).
"""
import wave
import numpy as np
import pylab as pl
import pyaudio

chunk = 1024

wf = wave.open(r"d:\至少还有你.wav", "rb")
p = pyaudio.PyAudio()

#打开声音输出流
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

#写声音播放流进行播放
print "正在播放《至少还有你》"
while True:
    data = wf.readframes(chunk)
    if data == "":
        break
    stream.write(data)

stream.close()
print "播放结束，谢谢欣赏"
p.terminate()
