from __future__ import division
import  matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from random import randint
import os
import sys
import statsmodels.api as sm
from math import isnan, isinf


def randcolor():
    c1 = randint(0,255)
    c2 = randint(0,255)
    c3 = randint(0,255)

    clr = '#%02x%02x%02x' % (c1, c2, c3)
    return clr

def plot_dat(fig, mdat, ylab, clr, clim = 65):

    simlist = list(set(mdat['sim'].tolist()))
    print len(simlist)
    X = []
    Y = []
    for i, sim in enumerate(simlist):
        d = mdat[mdat['sim'] == sim]
        x = d['ct'].tolist()
        if ylab == '%Dormant':
            y = d[ylab].tolist()
        else:
            y = np.log10(d[ylab]).tolist()

        for ii, val in enumerate(y):
            if isnan(val) == False and isinf(val) == False:
                X.append(x[ii])
                Y.append(val)

    xran = np.arange(1, 2000, 1).tolist()
    binned = np.digitize(X, xran).tolist()
    bins = [list([]) for _ in xrange(2000)]

    for i, val in enumerate(binned):
        bins[val-1].append(Y[i])

    pct5 = []
    pct95 = []
    xran = []
    for i, _bin in enumerate(bins):
        if len(_bin) > 0:
            pct5.append(np.percentile(_bin, 100 - clim))
            pct95.append(np.percentile(_bin, clim))
            xran.append(i+1)

    if clr == '0.3':
        plt.fill_between(xran, pct5, pct95, facecolor= clr, alpha=0.82, lw=0.2)
    else:
        plt.fill_between(xran, pct5, pct95, facecolor= clr, alpha=0.5, lw=0.2)

    return fig


mydir = os.path.expanduser('~/GitHub/Micro-Encounter')
sys.path.append(mydir+'/tools')
mydir2 = os.path.expanduser("~/")
df = pd.read_csv(mydir + '/results/simulated_data/2016_09_21_SimData-TSA.csv')

#-------------------------DATA TRANSFORMATIONS -----------------------

df['%Dormant'] = 100*df['DormantN']/df['N']


#### plot figure ###############################################################
fig = plt.figure()
fs = 8 # fontsize
xlimit = 2000
xlab = 'Generations'

#### PLOT 1 #################################################################
dat = pd.DataFrame(df)

dat = dat[dat['SpatialComplexity'].str.contains('-chemotaxis-')]

dat1 = dat[dat['ResourceComplexity'].str.contains('-lockandkey-')]

dat2 = dat[dat['ResourceComplexity'].str.contains('-polyculture-')]
dat2 = dat2[dat2['ResourceComplexity'].str.contains('-simple-')]

dat3 = dat[dat['ResourceComplexity'].str.contains('-monoculture-')]
dat3 = dat3[dat3['ResourceComplexity'].str.contains('-simple-')]

fig.add_subplot(3, 3, 1)

plt.plot([0, 1], [-10, -10], c = '0.3', ls = '-', alpha = 0.5, lw=10, label='Lock&Key')
plt.plot([0, 1], [-10, -10], c = 'm', ls = '-', alpha = 0.5, lw=10, label='Polyculture')
plt.plot([0, 1], [-10, -10], c = 'c', ls = '-', alpha = 0.5, lw=10, label='Monoculture')

ylab = '$log$'+r'$_{10}$'+'($Encounters$)'
datylab = 'Encounters'

fig = plot_dat(fig, dat3, datylab, 'c')
fig = plot_dat(fig, dat2, datylab, 'm')
fig = plot_dat(fig, dat1, datylab, '0.3')

plt.ylabel(ylab, fontsize=fs+1)
plt.xlabel(xlab, fontsize=fs+1)
plt.ylim(-0.1, 2.1)
plt.tick_params(axis='both', which='major', labelsize=fs-1)

plt.text(300, -1.3, 'Chemotaxis', fontsize=fs+6)

plt.legend(bbox_to_anchor=(-0.05, 1.14, 3.9, .2), loc=10, ncol=3, mode="expand",prop={'size':fs+3})


#### PLOT 2 #################################################################
fig.add_subplot(3, 3, 2)

dat = pd.DataFrame(df)
dat = dat[dat['SpatialComplexity'].str.contains('-randwalk-')]

dat1 = dat[dat['ResourceComplexity'].str.contains('-lockandkey-')]

dat2 = dat[dat['ResourceComplexity'].str.contains('-polyculture-')]
dat2 = dat2[dat2['ResourceComplexity'].str.contains('-simple-')]

dat3 = dat[dat['ResourceComplexity'].str.contains('-monoculture-')]
dat3 = dat3[dat3['ResourceComplexity'].str.contains('-simple-')]

ylab = '$log$'+r'$_{10}$'+'($Encounters$)'
datylab = 'Encounters'

fig = plot_dat(fig, dat3, datylab, 'c')
fig = plot_dat(fig, dat2, datylab, 'm')
fig = plot_dat(fig, dat1, datylab, '0.3')

plt.ylabel(ylab, fontsize=fs+1)
plt.xlabel(xlab, fontsize=fs+1)
plt.ylim(-0.1, 2.1)
plt.tick_params(axis='both', which='major', labelsize=fs-1)

plt.text(100, -1.3, 'Run and tumble', fontsize=fs+6)

#### PLOT 3 #################################################################
fig.add_subplot(3, 3, 3)

dat = pd.DataFrame(df)
dat = dat[dat['SpatialComplexity'].str.contains('-none-')]

dat1 = dat[dat['ResourceComplexity'].str.contains('-lockandkey-')]

dat2 = dat[dat['ResourceComplexity'].str.contains('-polyculture-')]
dat2 = dat2[dat2['ResourceComplexity'].str.contains('-simple-')]

dat3 = dat[dat['ResourceComplexity'].str.contains('-monoculture-')]
dat3 = dat3[dat3['ResourceComplexity'].str.contains('-simple-')]

ylab = '$log$'+r'$_{10}$'+'($Encounters$)'
datylab = 'Encounters'

fig = plot_dat(fig, dat3, datylab, 'c')
fig = plot_dat(fig, dat2, datylab, 'm')
fig = plot_dat(fig, dat1, datylab, '0.3')

plt.ylabel(ylab, fontsize=fs+1)
plt.xlabel(xlab, fontsize=fs+1)
plt.ylim(-0.1, 2.1)
plt.tick_params(axis='both', which='major', labelsize=fs-1)

plt.text(500, -1.3, 'Passive', fontsize=fs+6)



#### PLOT 4 #################################################################
dat = pd.DataFrame(df)
dat = dat[dat['TrophicComplexity'].str.contains('-none-')]

dat1 = dat[dat['ResourceComplexity'].str.contains('-lockandkey-')]

dat2 = dat[dat['ResourceComplexity'].str.contains('-polyculture-')]
dat2 = dat2[dat2['ResourceComplexity'].str.contains('-simple-')]

dat3 = dat[dat['ResourceComplexity'].str.contains('-monoculture-')]
dat3 = dat3[dat3['ResourceComplexity'].str.contains('-simple-')]

fig.add_subplot(3, 3, 4)

plt.plot([0, 1], [-10, -10], c = '0.3', ls = '-', alpha = 0.5, lw=10, label='Lock&Key')
plt.plot([0, 1], [-10, -10], c = 'm', ls = '-', alpha = 0.5, lw=10, label='Polyculture')
plt.plot([0, 1], [-10, -10], c = 'c', ls = '-', alpha = 0.5, lw=10, label='Monoculture')

ylab = '$log$'+r'$_{10}$'+'($Encounters$)'
datylab = 'Encounters'

fig = plot_dat(fig, dat3, datylab, 'c')
fig = plot_dat(fig, dat2, datylab, 'm')
fig = plot_dat(fig, dat1, datylab, '0.3')

plt.ylabel(ylab, fontsize=fs+1)
plt.xlabel(xlab, fontsize=fs+1)
plt.ylim(-0.1, 2.1)
plt.tick_params(axis='both', which='major', labelsize=fs-1)

plt.text(600, -1.3, 'Simple', fontsize=fs+6)

#plt.legend(bbox_to_anchor=(-0.05, 1.14, 3.9, .2), loc=10, ncol=3, mode="expand",prop={'size':fs+3})


#### PLOT 5 #################################################################
fig.add_subplot(3, 3, 5)

dat = pd.DataFrame(df)
dat = dat[dat['TrophicComplexity'].str.contains('-crossfeeding-')]

dat1 = dat[dat['ResourceComplexity'].str.contains('-lockandkey-')]

dat2 = dat[dat['ResourceComplexity'].str.contains('-polyculture-')]
dat2 = dat2[dat2['ResourceComplexity'].str.contains('-simple-')]

dat3 = dat[dat['ResourceComplexity'].str.contains('-monoculture-')]
dat3 = dat3[dat3['ResourceComplexity'].str.contains('-simple-')]

ylab = '$log$'+r'$_{10}$'+'($Encounters$)'
datylab = 'Encounters'

fig = plot_dat(fig, dat3, datylab, 'c')
fig = plot_dat(fig, dat2, datylab, 'm')
fig = plot_dat(fig, dat1, datylab, '0.3')

plt.ylabel(ylab, fontsize=fs+1)
plt.xlabel(xlab, fontsize=fs+1)
plt.ylim(-0.1, 2.1)
plt.tick_params(axis='both', which='major', labelsize=fs-1)

plt.text(250, -1.3, 'Crossfeeding', fontsize=fs+6)

#### PLOT 6 #################################################################
fig.add_subplot(3, 3, 6)

dat = pd.DataFrame(df)
dat = dat[dat['TrophicComplexity'].str.contains('-scavenging-')]

dat1 = dat[dat['ResourceComplexity'].str.contains('-lockandkey-')]

dat2 = dat[dat['ResourceComplexity'].str.contains('-polyculture-')]
dat2 = dat2[dat2['ResourceComplexity'].str.contains('-simple-')]

dat3 = dat[dat['ResourceComplexity'].str.contains('-monoculture-')]
dat3 = dat3[dat3['ResourceComplexity'].str.contains('-simple-')]

ylab = '$log$'+r'$_{10}$'+'($Encounters$)'
datylab = 'Encounters'

fig = plot_dat(fig, dat3, datylab, 'c')
fig = plot_dat(fig, dat2, datylab, 'm')
fig = plot_dat(fig, dat1, datylab, '0.3')

plt.ylabel(ylab, fontsize=fs+1)
plt.xlabel(xlab, fontsize=fs+1)
plt.ylim(-0.1, 2.1)
plt.tick_params(axis='both', which='major', labelsize=fs-1)

plt.text(400, -1.3, 'Scavenging', fontsize=fs+6)


#### Final Format and Save #####################################################
plt.subplots_adjust(wspace=0.4, hspace=0.8)
plt.savefig(mydir + '/results/figures/TimeSeries-ResourceEffectsOnEncounters.png', dpi=600, bbox_inches = "tight")
plt.close()
