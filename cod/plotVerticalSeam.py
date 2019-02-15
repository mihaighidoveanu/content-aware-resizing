import numpy as np
import matplotlib.pyplot as plt


def plotVerticalSeam(img,E,seam,colorSeam):
#plot the vertical seam in the image
#
#input: img - initial image
#       E - energy at each pixel computer after image gradient
#       seam - the seam connecting top to bottom
#       colorSeam  - specifies the color to draw the seam in. Possible values : 
#                    [r b g]' -  RGB triplets, transposed as column arrays(e.g [255 0 0]' - red)          

	imgPlotted = img
	for i in range(0, np.shape(seam)[0] ):
	    imgPlotted[seam[i, 0], seam[i,1], :] = np.uint8(colorSeam)
	asasdas
	plt.figure()

	#full screen
	#figure('units','normalized','outerposition',[0 0 1 1])
	plt.subplot(1,2,1)
	plt.imshow(imgPlotted)
	plt.subplot(1,2,2)
	plt.imshow(E)