#!/usr/bin/env python
import sys,os
import numpy as np
import pandas as pd
import copy

#--matplotlib
import matplotlib
matplotlib.use('Agg')
import pylab as py
from  matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text',usetex=True)
matplotlib.rcParams['text.latex.preamble'] = [r'\usepackage{color}']

from tools import load

nrows,ncols=2,2
fig = py.figure(figsize=(ncols*4,nrows*2.5))

##########################################################
wdir='run27'
I=load('%s/data/valid_replicas.dat'%wdir)
dataf =load('%s/data/raamc-full.dat'%wdir)
IDX=sorted(dataf.keys())
for idx in IDX:
    dataf[idx]['replicas']=np.array(dataf[idx]['replicas'])

####################################################
ax2=py.subplot(nrows,ncols,2)
for idx in IDX:
    col= dataf[idx]['col'][0]
    R=dataf[idx]['R'][0]
    print col,R
    if dataf[idx]['R'][0]!=0.2: continue
    pT=dataf[idx]['pT']
    value=dataf[idx]['value']
    alpha=dataf[idx]['alpha']
    if col=='ALICE': ax2.errorbar(pT,value,alpha,fmt='ko',label=r'$\rm ALICE$')
    if col=='CMS': ax2.errorbar(pT,value,alpha,fmt='ko',mfc='white',label=r'$\rm CMS$')
    fmax=np.amax(dataf[idx]['replicas'][I],axis=0)
    fmin=np.amin(dataf[idx]['replicas'][I],axis=0)
    ax2.fill_between(pT,fmin,fmax,facecolor='None',edgecolor='r',hatch='/////')

##########################################################
ax1=py.subplot(nrows,ncols,1)
for idx in IDX:
    col= dataf[idx]['col'][0]
    R=dataf[idx]['R'][0]
    print col,R
    if dataf[idx]['R'][0]!=0.4: continue
    pT=dataf[idx]['pT']
    value=dataf[idx]['value']
    alpha=dataf[idx]['alpha']
    if col=='ATLAS': ax1.errorbar(pT,value,alpha,fmt='ko',label=r'$\rm ATLAS$')
    if col=='CMS': ax1.errorbar(pT,value,alpha,fmt='ko',mfc='white',label=r'$\rm CMS$')
    fmax=np.amax(dataf[idx]['replicas'][I],axis=0)
    fmin=np.amin(dataf[idx]['replicas'][I],axis=0)
    ax1.fill_between(pT,fmin,fmax,facecolor='None',edgecolor='r',hatch='/////')


##########################################################
wdir='run50'
I=load('%s/data/valid_replicas.dat'%wdir)
dataf =load('%s/data/raamc-full.dat'%wdir)
IDX=sorted(dataf.keys())
for idx in IDX:
    dataf[idx]['replicas']=np.array(dataf[idx]['replicas'])


####################################################
ax4=py.subplot(nrows,ncols,4)
for idx in IDX:
    col= dataf[idx]['col'][0]
    R=dataf[idx]['R'][0]
    if dataf[idx]['R'][0]!=0.2: continue
    pT=dataf[idx]['pT']
    value=dataf[idx]['value']
    alpha=dataf[idx]['alpha']
    if col=='ALICE': ax4.errorbar(pT,value,alpha,fmt='k^',mfc='white',label=r'$\rm ALICE$')
    fmax=np.amax(dataf[idx]['replicas'][I],axis=0)
    fmin=np.amin(dataf[idx]['replicas'][I],axis=0)
    ax4.fill_between(pT,fmin,fmax,facecolor='None',edgecolor='r',hatch='/////')

##########################################################
ax3=py.subplot(nrows,ncols,3)
for idx in IDX:
    col= dataf[idx]['col'][0]
    R=dataf[idx]['R'][0]
    print col,R
    if dataf[idx]['R'][0]!=0.4: continue
    pT=dataf[idx]['pT']
    value=dataf[idx]['value']
    alpha=dataf[idx]['alpha']
    if col=='ATLAS': ax3.errorbar(pT,value,alpha,fmt='ko',label=r'$\rm ATLAS$')
    if col=='ALICE': ax3.errorbar(pT,value,alpha,fmt='k^',mfc='white',label=r'$\rm ALICE$')
    fmax=np.amax(dataf[idx]['replicas'][I],axis=0)
    fmin=np.amin(dataf[idx]['replicas'][I],axis=0)
    ax3.fill_between(pT,fmin,fmax,facecolor='None',edgecolor='r',hatch='/////')


AX=[ax1,ax2,ax3,ax4]
for ax in AX:
    ax.legend(fontsize=18,loc=4,frameon=0,handletextpad=0.01)
    ax.set_ylim(0,1)
    ax.tick_params(axis='both', which='major', labelsize=20,direction="in")
    ax.set_yticks([0,0.2,0.4,0.6,0.8,1])


AX=[ax2,ax4]
for ax in AX:
    ax.set_yticklabels([])

ax1.set_ylabel(r'\boldmath${\rm R_{\rm AA}}$',size=20)
ax4.set_xlabel(r'\boldmath$p_{\rm T}~[\rm GeV]$',size=20)
ax4.xaxis.set_label_coords(0.85, -0.03)

ax3.set_xticks([200,400,600,800])
ax3.set_xticklabels([r'$200$',r'$400$',r'$600$',r'$800$'])
ax4.set_xticks([50,70,90,110])
ax4.set_xticklabels([r'$50$',r'$70$',r'$90$',r''])

ax1.text(0.2,0.1,r'$R=0.4$',transform=ax1.transAxes,size=20)
ax2.text(0.2,0.1,r'$R=0.2$',transform=ax2.transAxes,size=20)
ax3.text(0.2,0.1,r'$R=0.4$',transform=ax3.transAxes,size=20)
ax4.text(0.2,0.1,r'$R=0.2$',transform=ax4.transAxes,size=20)


ax1.text(0.2,0.82,r'$\sqrt{s_{\rm NN}}=2.76~{\rm TeV}$',transform=ax1.transAxes,size=20)
ax3.text(0.2,0.82,r'$\sqrt{s_{\rm NN}}=5.02~{\rm TeV}$',transform=ax3.transAxes,size=20)



#py.tight_layout()
py.subplots_adjust(left=0.1, bottom=0.08, right=0.99, top=0.97, wspace=0, hspace=None)
py.savefig('fig1.pdf')
py.close()


