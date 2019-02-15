from __future__ import print_function
import matplotlib.pyplot as plt

from computeEnergy import computeEnergy
from selectVerticalSeam import selectVerticalSeam
from plotVerticalSeam import plotVerticalSeam
from deleteVerticalSeam import deleteVerticalSeam

def reduceWidth(img,params) :
#reduces image width by params.nrPixels (deletes seams from top to bottom)
#
#input: img - initial image
#       params :
#          nrPixels - number of seams to delete ( a seam has width of 1 pixel)
#           selectSeam - the method of selecting which seams to delete. Possible values:
#                               'random',
#                               'greedy',
#                               'programareDinamica'
#           plotSeam - specifies wether the seam will be plotted or not (Boolean value)
#           colorSeam  - specifies color of seams. Possible values
#                        [r g b]' -  RGB triplets, transposed as column arrays (e.g [255 0 0]' - red)          
#                               
# output: img - resized Image

    for i in  range(0, params.nrPixels) :
    
        print('Deleting vertical seam No. ', i,' from a total of ', params.nrPixels)

        #compute energy after the formula (1) from the article
        E = computeEnergy(img)
        
        #alege drumul vertical care conecteaza sus de jos
        drum = selectVerticalSeam(E,params.selectSeam)
        
        #afiseaza drum
        if params.plotSeam :
            plotVerticalSeam(img,E,drum,params.colorSeam)
            plt.pause(1)
            plt.close()
        
        #elimina drumul din imagine
        img = deleteVerticalSeam(img,drum)

    return img 
