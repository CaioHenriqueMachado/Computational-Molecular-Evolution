# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 17:49:06 2018

@author: caiom
"""

from pylab import * 

grafico_x = [0,5,10,20,30,40,50,60,70,80,90,100]
grafico_y = [100,58,27,9,6,5.94,5.63,5.51,5.46,5.32,5.33,5.39] 

plt.rcParams['figure.figsize'] = (12,8)

plt.title('AFINIDADE X MUTAÇÃO')
plt.plot( grafico_x , grafico_y, c='#0000ff',lw=3)
plt.xlabel('Mutação(%)')
plt.ylabel('Afinidade(%)')
plt.grid(True)

plt.show()