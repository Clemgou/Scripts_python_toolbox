#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################################ 
# IMPORTATIONS
################################################################################################

import matplotlib.pyplot as plt
import numpy as np
from   numpy.fft  import fft2, ifft2

################################################################################################ 
# FUNCTIONS
################################################################################################

def np_fftconvolve(A, B):
    '''
    Quick method to compute 2D convolution.
    '''
    return np.real(ifft2(fft2(A)*fft2(B, s=A.shape)))

def background(modeIntensityProfile):
    '''
    Return the background of the modeIntensityProfile.
    modeIntensityProfile must be a 2D np.arrays.
    
    Function to be imporved to return more reliable background, eg using quadratic method.
    '''
    return np.min(modeIntensityProfile)

def normalise(modeIntensityProfile):
    '''
    Normalizing the mode profile
    '''
    back_grd = background(modeIntensityProfile) # background
    peak_max = np.max(modeIntensityProfile) # peak
    modeIntensityProfile = (modeIntensityProfile-back_grd)/(peak_max-back_grd) # normalised picture mode (2D array)
    # ---  --- #
    return modeIntensityProfile

def overlap(img_mode_fiber, img_mode_wvgud, normalise_fiber=True):
    '''
    return the overlap of the e-field from the two image of the intensity mode.
    The intensity modes img_mode_fiber, img_mode_fiber, must be 2D np.arrays.
    '''
    # --- Normalisation --- #
    if normalise_fiber:
        img_mode_fiber_norm = normalise(img_mode_fiber)
    else:
        img_mode_fiber_norm = img_mode_fiber
    # ---  --- #
    img_mode_wvgud_norm = normalise(img_mode_wvgud)
    
    # --- compute E-field from intensity mode --- #
    efield_fiber = np.sqrt(img_mode_fiber_norm)
    efield_fiber = efield_fiber/np.sqrt(np.sum(efield_fiber**2))
    
    efield_wvgud = np.sqrt(img_mode_wvgud_norm)
    efield_wvgud = efield_wvgud/np.sqrt(np.sum(efield_wvgud**2))
    # --- compute the overlap by making the convolution of the two fields --- #
    #ovrlp = np.max(scipy.signal.convolve2d(efield_fiber, efield_wvgud))**2 # very slow !!!
    ovrlp = np.max( np_fftconvolve(efield_fiber, efield_wvgud) )**2
    return ovrlp


################################################################################################
# CODE
################################################################################################
if __name__=='__main__':
    import os
    from   PIL import Image
    path   = './'
    img_wvgud = np.array(Image.open(path+'mode_SWG_example.tif'))
    img_fiber = np.array(Image.open(path+'mode_SWG_FIBER_example.tif'))

    print(overlap(img_fiber, img_wvgud))
