# -*- coding: utf-8 -*-
"""modeloSIR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Kg1Aau_YQTMnwz6b06JiRLJAYU2k6A1B
"""

import numpy as np
from matplotlib import pyplot as plt

p = 1200
a = 0.001
b = 0.6
periodo = 25

n = np.linspace(0, periodo, periodo+1)
s = np.zeros(periodo+1)
i = np.zeros(periodo+1)
r = np.zeros(periodo+1)

i[0] = 10
s[0] = 1200 - i[0]
r[0]= 0

for t in range(periodo):
  s[t+1] = (s[t]) - (a*s[t]*i[t])
  i[t+1] = (i[t]) + (a*s[t]*i[t]) - (b*i[t])
  r[t+1] = (r[t]) + (b*i[t])
  print(i[t])

plt.plot(n, i)
plt.plot(n, s)
plt.plot(n, r)