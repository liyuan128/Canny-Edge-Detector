
import numpy as np

def threshold(img):

	# variables to store images for 10, 30 and 50 percent
	histogram = [0] * 256
	height, width = img.shape
	img10 = np.zeros((height, width))
	img30 = np.zeros((height, width))
	img50 = np.zeros((height, width))

	# loop for finding histogram of the image
	i = 0
	while i < height:
		j = 0
		while j < width:
			if int(img[i][j]) > 0:
				histogram[int(img[i][j])] = histogram[int(img[i][j])] + 1
			j = j + 1
		i = i + 1

	# threshold image for 10, 30 and 50 percent
	img10 = pTile(histogram, img, 10)
	img30 = pTile(histogram, img, 30)
	img50 = pTile(histogram, img, 50)

	# return 3 images after thresholding
	return img10, img30, img50

def pTile(histogram, img, percentage):

	# variable to store total pixel count of the image
	height, width = img.shape
	imgOut = np.zeros((height, width))
	totalPixelCount = 0
	threshold = 0

	# calculate total pixel count
	i = 0
	while i < len(histogram):
		totalPixelCount = totalPixelCount + histogram[i]
		i = i + 1


	# find specific percent of pixels of total pixel count
	pixelCountThreshold = int(totalPixelCount * ((100 - percentage) / 100.0))

	# find the threshold in range [0, 255]
	freqDash = 0
	i = 0
	while i < len(histogram):
		if freqDash > pixelCountThreshold:
			threshold = i
			break
		freqDash = freqDash + histogram[i]
		i = i + 1

	print("threshold: " + str(threshold))

	# loop to threshold the image 
	i = 0
	edgePixelCount = 0
	while i < height:
		j = 0
		while j < width:
			if img[i][j] < threshold:
				imgOut[i][j] = 0
			else:
				edgePixelCount = edgePixelCount + 1
				imgOut[i][j] = 255
			j = j + 1
		i = i + 1

	print("edge pixels: " + str(edgePixelCount))
	return imgOut
