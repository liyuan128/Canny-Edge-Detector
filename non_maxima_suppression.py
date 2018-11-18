
import numpy as np

def non_maxima_suppression(img, imgTheta):

	# setting startI and startJ to 4, 4 assuming gaussian filter size of 7 X 7
	startI, startJ = 4, 4
	i, j = startI, startJ
	height, width = img.shape
	imgOut = np.zeros((height, width))

	# variables for storing i, j values after finding direction of theta
	prevI, prevJ = 0, 0
	nextI, nextJ = 0, 0

	# loop for iterating over each pixel of the image
	while i < height - startI:
		j = startJ
		while j < width - startJ:
			prevI, prevJ, nextI, nextJ = getDirection(imgTheta[i][j], i, j)
			if img[i][j] < img[prevI][prevJ] or img[i][j] < img[nextI][nextJ]:
				imgOut[i][j] = 0
			else:
				imgOut[i][j] = img[i][j]
			j = j + 1
		i = i + 1

	# return new image after performing non maxima suppression
	return imgOut


# function to find sector according to given angle
def getDirection(angle, i, j):

	#for sector 0
	if (angle > 337.5 or angle <= 22.5) or (angle > 157.5 and angle <= 202.5):
		return i, j-1, i, j+1

	#for sector 1
	elif (angle > 22.5 and angle <= 67.5) or (angle > 202.5 and angle <= 247.5):
		return i+1, j-1, i-1, j+1

	#for sector 2
	elif(angle > 67.5 and angle <= 112.5) or (angle > 247.5 and angle <= 292.5):
		return i-1, j, i+1, j

	#for sector 3
	elif(angle > 112.5 and angle <= 157.5) or (angle > 292.5 and angle <= 337.5):
		return i-1, j-1, i+1, j+1


