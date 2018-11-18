
import cv2 
from gaussian_smoothing import gaussian_smoothing
from compute_gradient import compute_gradient
from non_maxima_suppression import non_maxima_suppression
from threshold import threshold
import sys
from pathlib import Path


def main():

	# Read RGB image as GRAYSCALE
	imageName = sys.argv[1]


	img = cv2.imread(imageName, cv2.IMREAD_GRAYSCALE)

	# check if image exists or not. If image does not exists img contains None value
	if img == None:
		print("Image does not exists!")
		sys.exit() 

	# removing the extension and storing only name of the image
	imageName = imageName.split(".")[0]

	# filter the image using gaussian smoothing
	img = gaussian_smoothing(img)
	cv2.imwrite(imageName + "-" + "gaussian.png", img)

	# compute image gradient
	imgGX, imgGY, img, imgTheta = compute_gradient(img)
	cv2.imwrite(imageName + "-" + "gradient-X.png", imgGX)
	cv2.imwrite(imageName + "-" + "gradient-Y.png", imgGY)
	cv2.imwrite(imageName + "-" + "gradient.png", img)

	# find non maxima suppression of given image and return new image and theta values of each pixel in a matrix
	img = non_maxima_suppression(img, imgTheta)
	cv2.imwrite(imageName + "-" + "maxima.png", img)

	# remove unwanted pixels by setting them to zero by using simple thresholding
	img10, img30, img50 = threshold(img)
	cv2.imwrite(imageName + "-" + "ptile10.png", img10)
	cv2.imwrite(imageName + "-" + "ptile30.png", img30)
	cv2.imwrite(imageName + "-" + "ptile50.png", img50)

	# show final image on screen
	# cv2.imshow(imageName, img)

	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

if __name__ == "__main__":
	main()