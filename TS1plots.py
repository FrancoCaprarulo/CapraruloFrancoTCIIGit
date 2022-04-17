# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 17:48:22 2022

@author: fcfra
"""

from scipy import signal
import matplotlib.pyplot as plt

num = [1, -1]
den = [1, 1]
sys = signal.TransferFunction(num, den)
w, mag, phase = signal.bode(sys)
plt.figure()
plt.semilogx(w, mag)    # Bode magnitude plot
plt.ylim(-1,1)
plt.figure()
plt.semilogx(w, phase)  # Bode phase plot
plt.xlim(0.01 , 100)
plt.show()