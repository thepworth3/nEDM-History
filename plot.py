# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 00:01:04 2025

@author: Thomas Hepworth (thomashepworth12@gmail.com email for questions)
"""

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker
import numpy as np

df = pd.read_csv("data.csv", sep=",")  # specify path as needed

year = df.Year
nEDM = df.nEDM
lab = df.Lab
experiment = df.Experiment

# we want to write these into different data files based on the Lab, to have unique labels
#any new measurement, or a specifc prediction can be added to a row in "data.csv". If the lab is a new
#name tag, or an existing lab uses a method new to them, create the coresponding empty lists and add required elif
#to manage the data


# empty lists
year_ILL_UCN = []
nEDM_ILL_UCN = []
year_ILL_CN = []
nEDM_ILL_CN = []
year_ANL = []
nEDM_ANL = []
year_ORNL = []
nEDM_ORNL = []
year_MIT_BNL = []
nEDM_MIT_BNL = []
year_BNL = []
nEDM_BNL = []
year_PNPI = []
nEDM_PNPI = []
year_PSI = []
nEDM_PSI = []

#sort data
for i in range(len(lab)):
    if lab[i] == "ILL" and experiment[i] == "Cold neutron beam":
        year_ILL_CN.append(year[i])
        nEDM_ILL_CN.append(nEDM[i])
    elif lab[i] == "ILL" and experiment[i] == "UCN":
        year_ILL_UCN.append(year[i])
        nEDM_ILL_UCN.append(nEDM[i])
    elif lab[i] == "ANL":
        year_ANL.append(year[i])
        nEDM_ANL.append(nEDM[i])
    elif lab[i] == "ORNL":
        year_ORNL.append(year[i])
        nEDM_ORNL.append(nEDM[i])
    elif lab[i] == "MIT/BNL":
        year_MIT_BNL.append(year[i])
        nEDM_MIT_BNL.append(nEDM[i])
    elif lab[i] == "BNL":
        year_BNL.append(year[i])
        nEDM_BNL.append(nEDM[i])
    elif lab[i] == "PNPI":
        year_PNPI.append(year[i])
        nEDM_PNPI.append(nEDM[i])
    elif lab[i] == "PSI":
        year_PSI.append(year[i])
        nEDM_PSI.append(nEDM[i])

# now all this data can be given common symbols on a legend!!



#plotting
plt.rc('font', family='Times New Roman', size=14)  # set default font of your preference


fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, dpi=100, figsize = (8,6), gridspec_kw={
    'height_ratios': [15, 2]})  # adjust height ratio and size if you like!
fig.subplots_adjust(hspace=0.05) #space bewteen shaded regions

y = 1e-27

# data
# plotting each part and labelling
ax1.semilogy(year_ANL, nEDM_ANL, "bs", label="ANL (neutron scattering)")
ax1.semilogy(year_MIT_BNL, nEDM_MIT_BNL, "yh", label="MIT/BNL (Bragg reflection)")
ax1.semilogy(year_ORNL, nEDM_ORNL, "k^", label="ORNL (cold neutron beam)")

ax1.semilogy(year_BNL, nEDM_BNL, "mX", label="BNL (cold neutron beam)")
ax1.semilogy(year_ILL_CN, nEDM_ILL_CN, "gv", label="ILL (cold neutron beam)")
ax1.semilogy(year_PNPI, nEDM_PNPI, "bD", label="PNPI (UCN)")
ax1.semilogy(year_ILL_UCN, nEDM_ILL_UCN, "rv", label="ILL (UCN)")
ax1.semilogy(year_PSI, nEDM_PSI, "g*", label="PSI (UCN)")
#include line for current gen experiment
# ax1.axhline(y=2e-27, color='r', linestyle='--')
#ax1.text(1995, 1.4e-27, "TUCAN, others") TUCAN line if you want!!!!!


ax2.semilogy(year_ANL, nEDM_ANL, "bs", label="ANL (neutron scattering)")
ax2.semilogy(year_MIT_BNL, nEDM_MIT_BNL, "yh", label="MIT/BNL (Bragg reflection)")
ax2.semilogy(year_ORNL, nEDM_ORNL, "k^", label="ORNL (cold neutron beam)")
ax2.semilogy(year_BNL, nEDM_BNL, "mX", label="BNL (cold neutron beam)")
ax2.semilogy(year_ILL_CN, nEDM_ILL_CN, "gv", label="ILL (cold neutron beam)")
ax2.semilogy(year_PNPI, nEDM_PNPI, "bD", label="PNPI (UCN)")
ax2.semilogy(year_ILL_UCN, nEDM_ILL_UCN, "rv", label="ILL (UCN)")
ax2.semilogy(year_PSI, nEDM_PSI, "g*", label="PSI (UCN)")

ax1.legend()

# shaded regions to show predictions
ax1.fill_between(year, 4e-26, 1e-28, color="y")
ax2.fill_between(year, 5e-31, 1e-32, color="c")
ax1.text(1951, 5e-27, "SUSY ($\Phi$ ~ $\\alpha$/$\pi$) Predictions")
ax2.text(1951, 0.5e-31, "Standard Model Predictions")


#some tick management
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

# make the slash cutoffs on vertical axis and set the region which you cut from vertical axis
ax1.set_ylim(1e-28, 1e-17)
ax2.set_ylim(1e-32, 5e-31)

d = 0.5
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)


# plot
ax1.plot()
ax2.plot()

# common axis labels on figure
fig.supxlabel('Year of Publication')
fig.supylabel('Neutron EDM Upper Limit [ecm]')


#setting major ticks and minor ticks
nticks = 12 #reduce number and major ticks will be every two decades. 11 makes this happen, while 12 is every decade. This will change depedning on fig size but I am not exactly sure how so you may need to experiment with numbers.
maj_loc = matplotlib.ticker.LogLocator(numticks=nticks)
min_loc = matplotlib.ticker.LogLocator(subs=np.arange(0, 1, 0.1), numticks = 12)
ax1.yaxis.set_major_locator(maj_loc)
ax1.yaxis.set_minor_locator(min_loc)
#because of ax2 having a small range, it automatically gets the desirec major and minor ticks
#if you want to change this, please consult the matplotlib documentation

plt.savefig("nEDM_history.png")
plt.show()



