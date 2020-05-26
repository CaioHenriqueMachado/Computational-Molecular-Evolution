# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 18:10:28 2018

@author: caiom
"""

from pylab import *

plt.rcParams['figure.figsize'] = (12,8)

grafico1_x = [0,10,20,30,40,50,60,70,80,90,100]
#grafico1_y = [100,98,96,95,92.7,90,83.7,75,58,22,3]
grafico1_y = [3,22,58,75,83.7,90,92.7,95,96,98,100]
plt.title('AFINIDADE X EFICIÊNCIA DE FILTRO')
plt.plot( grafico1_x , grafico1_y, c='#0000ff',lw=3)
plt.xlabel('EFICIÊNCIA DE FILTRO(%)')
plt.ylabel('Afinidade(%)')
plt.grid(True)

plt.show()
