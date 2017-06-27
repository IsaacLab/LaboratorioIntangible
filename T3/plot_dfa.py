#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import scipy.io
from matplotlib import pyplot as plt
from pyeeg import dfa as dfa

def plot_dfa(x, cut, step, Nfit):
    ix = np.arange(np.log2(len(x)/2), cut, -step)
    n = np.round(2**ix)
    [alpha, n, F] = dfa(x, L=n)
    index = int(len(n)-Nfit)
    P = np.polyfit(np.log(n[index:]),np.log(F[index:]), 1)
    plt.title("Alpha = {:0.2f}".format(alpha))
    plt.xlabel('n')
    plt.ylabel('F(n)')
    plt.loglog(n, F)
    plt.loglog(n[index:], np.power(n[index:], P[0])*np.exp(P[1]), 'r')
    return [alpha, n, F]


