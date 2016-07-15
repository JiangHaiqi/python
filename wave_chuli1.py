#-*-coding: utf-8 -*-
#Script Name:   wave_chuli.py
#Auther:        Haiqi Jiang
#Created:       15th July
#Last Modified:
#Version:
"""
This python script is aimed at processing the Music file(.wav) and drawing the corresponding
waveform.
"""


import wave
import numpy as np
import pylab as pl

#打开WAV文档
f = wave.open(r"d:\至少还有你.wav", "rb")

#读取格式信息
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]

#读取波形数据
str_data = f.readframes(nframes)
f.close()

#将波形数据转化为数组
wave_data = np.fromstring(str_data, dtype = np.short)
wave_data.shape = -1, 2
wave_data = wave_data.T
time = np.arange(0, nframes) * (1.0 / framerate)

#绘制波形
pl.subplot(211)
pl.plot(time, wave_data[0])
pl.subplot(212)
pl.plot(time, wave_data[1], color = 'g')
pl.xlabel("time(second)")
pl.show()
