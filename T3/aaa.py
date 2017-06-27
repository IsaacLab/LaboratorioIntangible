#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import scipy.io
from matplotlib import pyplot as plt
from pyeeg import dfa as dfa

def readFilePerceptualCrossing(filename):
    data = scipy.io.loadmat(filename)
    size = len(data['dataSeries'])
    series  = [data['dataSeries'][i][0] for i in range(size)]
    series  = np.array(series)[:,:,0]
    oppType = [data['dataOpponentType'][i][0] for i in range(size)]
    oppType = np.array(oppType)[:,0]
    return [series, oppType]


[series, oppType] = readFilePerceptualCrossing('dataPC-distance.mat')
#ax = plt.subplot(1,3,1)
#plt.title(oppType[0])
#plt.plot(series[0,:])
#ax = plt.subplot(1,3,2)
#plt.title(oppType[1])
#plt.plot(series[1,:])
#ax = plt.subplot(1,3,3)
#plt.title(oppType[2])
#plt.plot(series[2,:])

indexOscill = [i for i, x in enumerate(oppType) if x[0] == "FOX"]
indexHuman  = [i for i, x in enumerate(oppType) if x[0] == "Human"]
indexShadow = [i for i, x in enumerate(oppType) if x[0] == "TIMXELSHADOW"]
#typeFox = np.array([oppType[i][0]=='FOX' for i in range(len(oppType))])
seriesHuman=series[indexHuman,:]

cut=2
step=0.1
for i in range(0,128):
#    x = series[i,:]
    x = np.diff(series[i,:])
    ix = np.arange(np.log2(len(x)/2), cut, -step)
    n = np.round(2**ix)
    n = range(200,2000,100) #np.round(2**ix)
    [alpha, n, F] = dfa(x, L=n)
    beta = 2*alpha-1
    print(oppType[i]+"\t"+str(beta))
#    print("Serie "+str(i)+": "+str(beta)+" ("+oppType[i]+")")

#plt.figure()
#plt.plot(seriesHuman[18,:])