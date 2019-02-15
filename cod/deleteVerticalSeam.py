import numpy as np

def deleteVerticalSeam(img,seam) :
#deletes a vertical seam from the image
#input: img - initial image
#       seam - vertical seam to delete
#output img1 - initial image after deleting the seam
	
	### here was MATLAB size() instead of np.shape()
	img1 = np.zeros(np.shape(img),'uint8')

	for i in range(np.shape(img1)[0]):
	    col = seam[i, 1]

	    #copiem partea din stanga
	    img1[i,0 : col,:] = img[i,0 :col,:]
	    
	    #copiem partea din dreapta

	    #completati aici codul vostru

	return img1