#!/usr/bin/env python
import sys,os
import numpy as np
import pandas as pd
import copy

#--from tools
from tools import load


def get_par(wdir):
    """
    wdir = run27 (rs=2.76 TeV) run250 (rs=5.02 TeV)
    parameters order
        g N , q N  , g b  , q b  , q a  , g a 
    
    """
    par=[load('%s/mcsamples/%s'%(wdir,_)) for _ in os.listdir('%s/mcsamples'%wdir)]
    return np.array(par)

if __name__=='__main__':

    pr27 = get_par('run27')
    pr50 = get_par('run50')
    print pr27.shape
    print pr50.shape








