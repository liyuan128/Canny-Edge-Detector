
import numpy as np

# function to filter image using gaussian smoothing
def gaussian_smoothing(img):

	# gaussian filter of size 7X7
	filter = [[1,1,2,2,2,1,1],
			  [1,2,2,4,2,2,1],
			  [2,2,4,8,4,2,2],
			  [2,4,8,16,8,4,2],
			  [1,1,2,2,2,1,1],
			  [1,2,2,4,2,2,1],
			  [2,2,4,8,4,2,2]]

	startI, startJ = int(len(filter) / 2), int(len(filter[0]) / 2)
	i, j = startI, startJ

	# find height and width of image
	height, width = img.shape

	# create new matrix for storing image after doing gaussian filtering
	imgOut = np.zeros((height, width))

	# loop for iterating over each pixel and mutiply the sub-matrix by gaussian filter
	while i < height - startI:
		j = startJ
		while j < width - startJ:
			imgOut[i][j] = convolve_filter(filter, img, i, j, startI, startJ) / 140
			j = j + 1
		i = i + 1

	# return new image
	return imgOut


# function to multiply two matrices
def convolve_filter(filter, img, i, j, startI, startJ):

	# variables for iterating over the matrix
	fI, fJ = 0, 0
	i = i - startI
	j = j - startJ
	saveJ = j
	sum = 0

	# loop for multiplying sub-matrix with gaussian matrix over given [i-startI...i+startI, j-startJ...j+startJ] range
	while fI < len(filter):
		fJ = 0
		j = saveJ
		while fJ < len(filter[0]):
			sum = sum + filter[fI][fJ] * img[i][j]
			j = j + 1
			fJ = fJ + 1
		fI = fI + 1
		i = i + 1

	# return computed convolution value
	return sum
