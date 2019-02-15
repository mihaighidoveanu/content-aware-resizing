import matplotlib.pyplot as plt
import cv2

from resizeImage import resizeImage
from parameters import Params

#ImageResize Project implemented after
#the article "Seam Carving for Content-Aware Image Resizing", autori S.
#Avidan si A. Shamir 
##
# this function runs the whole project
# set up the parameters and the image to resize here

params = Params()

#read the image to resize
img = cv2.imread('../data/avion1.jpeg')

imgResized_new = resizeImage(img,params) 

#foloseste functia imresize pentru redimensionare traditionala
imgResized_old = cv2.resize(img,( np.shape(imgResized_new)[0], np.shape(imgResized_new)[1]))

#ploteaza imaginile obtinute
plt.figure()

#1. imaginea initiala
h1 = plt.subplot(1,3,1)
plt.imshow(img)
xsize = plt.getp(h1,'xlim')
ysize = plt.getp(h1,'ylim')
plt.xlabel('Original image')

#2. imaginea redimensionata cu pastrarea continutului
h2 = plt.subplot(1,3,2)
plt.imshow(imgResized_new)
plt.setp(h2, 'xlim', xsize, 'ylim', ysize)
plt.xlabel('New smart resize')

#3. imaginea obtinuta prin redimensionare traditionala
h3 = plt.subplot(1,3,3)
plt.imshow(imgResized_old)
plt.setp(h3, 'xlim', xsize, 'ylim', ysize)
plt.xlabel('Old resize')
