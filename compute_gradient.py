
import math
import numpy as np
import cv2

def compute_gradient(img):

	# Lists for storing prewitt's operator for Gx and Gy for finding gradient at each pixel location
	Gx = [[-1,0,1],
		  [-1,0,1],
		  [-1,0,1]]

	Gy = [[1,1,1],
		  [0,0,0],
		 [-1,-1,-1]]

	# setting startI and startJ to 4, 4 assuming gaussian filter size of 7 X 7
	startI, startJ = 4, 4

	# finding height and width of image
	height, width = img.shape

	# create two lists for storing gradient values of image for X and Y; gradient theta and final gradient of image
	imgGX = np.zeros((height, width))
	imgGY = np.zeros((height, width))
	imgTheta = np.zeros((height, width))
	imgOut = np.zeros((height, width))

	# create i and j for iterating over the image
	i = startI
	j = startJ

	# loop for iterating over each pixel of the image and computing its X and Y gradient
	while i < height - startI:
		j = startJ
		while j < width - startJ:

			# finding gradient for X-axis i.e. Gx and finding the absolute value of gradient
			imgGX[i][j] = multiply_matrices(img, Gx, i, j, int(len(Gx) / 2), int(len(Gx) / 2))
			if imgGX[i][j] < 0:
				imgGX[i][j] = abs(imgGX[i][j])

			# finding gradient for y-axis i.e. Gy and finding the absolute value of gradient
			imgGY[i][j] = multiply_matrices(img, Gy, i, j, int(len(Gy) / 2), int(len(Gy) / 2))
			if imgGY[i][j] < 0:
				imgGY[i][j] = abs(imgGY[i][j])

			# normalize X and Y gradient
			imgGX[i][j] = imgGX[i][j] / 3.0
			imgGY[i][j] = imgGY[i][j] / 3.0

			#calculating gradient for final image and dividing the gradient by root of 2 to normalize the image to [0,255]
			imgOut[i][j] = np.sqrt(np.power(imgGX[i][j], 2)  + np.power(imgGY[i][j], 2)) / np.sqrt(2) # compute normalized gradient for whole image

			# if X gradient is zero set theta to 90 or -90 depending upon Y gradient
			if imgGX[i][j] == 0:
				if imgGY[i][j] > 0:
					imgTheta[i][j] = 90
				else:
					imgTheta[i][j] = -90
			else:
				imgTheta[i][j] = math.degrees(math.atan((imgGY[i][j] / imgGX[i][j])))

			# if theta value is less than 0 then we need to round it to positive value to ease up the process of finding non-maxima suppression
			if imgTheta[i][j] < 0:
				imgTheta[i][j] = imgTheta[i][j] + 360
			j = j + 1
		i = i + 1
	
	# return gradients of image and theta values of each pixel
	return imgGX, imgGY, imgOut, imgTheta

def multiply_matrices(img, gradient, i, j, startI, startJ):

	#variables for iterating over gradient matrix
	gI, gJ = 0, 0

	#taking (i, j) as center of convolution, we shift left and up by half length of gradient
	i = i - startI
	j = j - startJ
	saveJ = j
	sum = 0

	# loop for multiplying sub-matrix with gaussian matrix over given [i-startI...i+startI, j-startJ...j+startJ] range
	while gI < len(gradient):
		gJ = 0
		j = saveJ
		while gJ < len(gradient[0]):
			sum = sum + (gradient[gI][gJ] * img[i][j])
			j = j + 1
			gJ = gJ + 1
		gI = gI + 1
		i = i + 1

	return sum

