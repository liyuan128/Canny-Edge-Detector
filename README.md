# Canny-Edge-Detector
Implementation of Canny Edge Detector algorithm

Key features:
1. Uses 7x7 gaussian filter to smooth the image
2. Uses prewitt's operator rather than using the conventional Robert's operator to compute gradient
3. Uses p-tile method to threshold the image
4. image thresholding done with 10%, 30% and 50% p-tile thresholding

File names: 			
1. main.py – file where processing of the algorithm starts
2. gaussian_smoothing.py - function to filter image using gaussian smoothing
3. compute_gradient.py - function to find gradient and theta values for each image pixel
4. non_maxima_suppression.py - function to find non maxima suppression for each of the image pixels
5. threshold.py - function to threshold image

Programming Language: 	Python 3

Instructions to run code:

1.	Program should be compiled using a Python 3 interpreter. 
2.	OpenCV and Numpy must be installed in the environment for the program to work, as OpenCV is used to read and write images and Numpy is used for array creation and basic mathematical functions.
3.	Algorithm starts processing from main.py, so make sure to call main.py only! Also, image name should be provided while interpreting the program along with the program file name. Moreover, image should be present in the current directory only.

eg Python3 main.py Lena256.bmp

4.	Run the code and required output images will be produced in the current directory as bitmap files (.bmp)

Images are saved as:
1.	Gaussian filtered image:
<image-name>-gaussian.bmp
2.	X-Gradient image:
<image-name>-gradient-X.bmp
3.	Y-Gradient image:
<image-name>-gradient-Y.bmp
4.	Magnitude gradient image:
<image-name>-gradient.bmp
5.	Non maxima suppressed image:
<image-name>-maxima.bmp
6.	P-tile 10% image:
<image-name>-ptile10.bmp
7.	P-tile 30% image:
<image-name>-ptile30.bmp
8.	P-tile 50% image:
<image-name>-ptile50.bmp
