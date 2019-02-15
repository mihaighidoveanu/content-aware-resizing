import numpy as np

class Params:

	#parameters for the main script .. here are the default values
	
	#resize option - one of 'reduceWidth', 'reduceHeight', 'increaseWidth', 'increaseHeight', 'removeObject'
	optionResize = 'reduceWidth';

	#resize the image with 20 pixels
	nrPixels = 20;

	#if to plot the seam or not
	plotSeam = True;

	#color of the seam, default red
	colorSeam = np.transpose([255, 0, 0])                       #---- this is matrix transposee'

	selectSeam = 'random';
	#possible options: 'random','greedy','dinamicProgramming'
