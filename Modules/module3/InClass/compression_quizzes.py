import matplotlib.pyplot as plt
import pydicom as dicom

from ipywidgets import interact
import ipywidgets as widgets

import skimage.io as io
import skimage.color as color
import numpy as np
import os

def win_lev(img, w, l, maxc=255):
    """
    Window (w) and level (l) data in img
    img: numpy array representing an image
    w: the window for the transformation
    l: the level for the transformation
    maxc: the maximum display color
    """

    m = maxc/(2.0*w)
    o = m*(l-w)
    return np.clip((m*img-o),0,maxc).astype(np.uint8)

def view_img_line(img):
    """
    """
    

    @interact(i=widgets.IntSlider(min=0, max=img.shape[1], value=img.shape[1]/2, step=4),
              win=widgets.IntSlider(min=1, max=2000, value=1000),
              level=widgets.IntSlider(min=-1024, max=2000, value=0))
    def _view_slice_roi(i=0, win=1000, level=0):
        f,(ax1,ax2) = plt.subplots(1,2)
        f.set_size_inches(8,4)
        t1 = color.gray2rgb(win_lev(img,win,level), alpha=True)
        io.imshow(t1,ax=ax2)
        ax2.grid(False)
        ax2.yaxis.set_visible(False)
        ax2.xaxis.set_visible(False)
        ax1.plot(img[:,i])
        ax2.axvline(x= i, color="red", linewidth=5, alpha=0.5) 
        plt.show()
        #sns.distplot(img[s1,j*dx:dx*(j+1),i*dx:dx*(i+1)])

def examine_img(fname=""):
    dimg = dicom.read_file(fname)
    img = dimg.pixel_array + dimg.RescaleIntercept

    view_img_line(img)
examine_img(os.path.join(os.path.expanduser("~"),"DATA/Images/PE/Ser_000006/IM-0124-0097.dcm"))
