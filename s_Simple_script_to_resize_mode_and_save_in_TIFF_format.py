#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################################ 
# IMPORTATIONS
################################################################################################

import numpy as np
from PIL import Image
import os

################################################################################################ 
# FUNCTIONS
################################################################################################


################################################################################################
# CODE
################################################################################################
if __name__=='__main__':
    h, w = 600, 600 # new format size
    
    path = './'
    name_L = os.listdir(path)
    for name in name_L:
        print(name)
        if name[-4:] == '.tif': #check if we have images and not other file type
            img   = np.array(Image.open(path+name))
            img_x = np.sum(img,axis=1) # histogram along x-axis
            img_y = np.sum(img,axis=0) # histogram along y-axis
            i0    = np.where(img_x == img_x.max())[0] # find roughly the index where the peak is
            j0    = np.where(img_y == img_y.max())[0] # find roughly the index where the peak is
            # new index to crop the image
            i_m   = int(i0[0] - h/2)
            i_M   = int(i0[0] + h/2)
            j_m   = int(j0[0] - w/2)
            j_M   = int(j0[0] + w/2)
            img_  = img[i_m:i_M , j_m:j_M]
            # save new image
            img_new = Image.fromarray(img_)
            new_name = name[:-4]+'_new.tif'
            img_new.save(path + new_name)

