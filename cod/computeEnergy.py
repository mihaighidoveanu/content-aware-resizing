import cv2
import numpy as np

def computeEnergy(img):
#compute energy of each pixel according to the gradient
#input: img - initial image
#output: E - energy cost	

	###transforming image to grayscale
	imgGray = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
	# imgShape = [[0 for col in range(len(imgGray[0]))] for row in range(len(imgGray))]

	###using a sobel filter to compute gradient over directions x and y
	gradX = cv2.Sobel(imgGray, cv2.CV_64F, 1, 0)
	#cv2.imwrite("gradX.jpg",gradX)

	gradY = cv2.Sobel(imgGray, cv2.CV_64F, 0, 1)
	#cv2.imwrite("gradY.jpg",gradY)

	###compute the magnitude of the gradient

	E = gradX + gradY

	#cv2.imwrite("magnitude.jpg",E)
	
	return E
	
	### E = energy - image gradient