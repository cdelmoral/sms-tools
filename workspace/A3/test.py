import numpy as np
from scipy.signal import get_window
import sys
sys.path.append('../../software/models/')
from dftModel import dftAnal, dftSynth

x = np.arange(10)
fs = 100000
M = x.size
w = get_window('hamming', M)
N = 1024

mX, pX = dftAnal(x, w, N)
y = dftSynth(mX, pX, M) * sum(w)