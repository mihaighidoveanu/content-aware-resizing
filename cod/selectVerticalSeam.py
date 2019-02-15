import numpy as np
from random import randint

def selectVerticalSeam(E,selectSeam):
# selects the vertical seam which minimies the cost function computer on E 
#
#input: E - energy at each pixel computed according to image gradient
#       selectSeam - chooses the way seams are selected. 
#                           'random' 
#                           'greedy' 
#                           'programareDinamica' 
#
#output: seam - the chosen vertical seam  

    seamShape = (np.shape(E)[0], 2)
    seam = np.zeros(seamShape, dtype = np.int8 )

    if selectSeam == 'random':

        #for first row we choose the first pixel randomly
        row = 1

        #we choose the column between 0 and size(E,2) - 1
        col = randint(0, np.shape(E)[1] - 1)

        #add to d the indexes of the first pixel in the seam
        seam[0, :] = [row, col]

        for i in range(1, np.shape(seam)[0]):

            #choose the next pixel according to the neighbours
            #row is i
            row = i

            #column depends of the column of the last pixel
            
            if seam[i-1, 1] == 1 :   #pixel is at the leftmost edge

                #two options
                option = randint(0,1)     #0 or 1 , with equal probabillity

            elif seam[i-1, 1] == np.shape(E)[1] :  #pixel is at the rightmost edge

                #two options
                option = randint(-1,0)  #-1 or 0 ,with equal probability

            else :
                option = randint(-1,1)  # -1, 0 or 1 ,with equal probability

            col = seam[i-1, 1] + option    #add up -1 , 0 or 1: 
                                            
            # go left, right or stay put
            seam[i,:] = [row, col]
        
    elif metodaSelectareDrum == 'greedy' :
        #to be
        print 2
    elif metodaSelectareDrum == 'programareDinamica' :
        #to be
        print 3
        
    else :
        error('Invalid option on how to select seams')

    return seam