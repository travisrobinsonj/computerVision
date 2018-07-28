"""
Live Sketch Using Webcam with OpenCv
"""
import cv2
import numpy as np

#sketch generation function
def sketch(image):
	"""
	:imput image and return image mask
	"""
	#convert image to gray scale
	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# use gaussian blur to clean up the image
	image_gray_blur = cv2.GaussianBlur(image_gray, (5,5) , 0)

	#edge extraction
	canny_edges = cv2.Canny(image_gray_blur, 10, 70)

	#do an invert binarize the image
	ret, mask = cv2.threshold(canny_edges, 70 , 255, cv2.THRESH_BINARY_INV)
	return mask
if __name__ == '__main__':

	#initialize the webcam, cap the object provided by the videoCapture
	#it contains a boolean indicating if it was successful (ret)
	# It also contains the images collected from the webcam (frame)
	cap = cv2.VideoCapture(0)

	while True:
		ret, frame = cap.read()
		cv2.imshow('Live sketcher image', sketch(frame))
		if cv2.waitKey(1) == 13 : # 13 is enter key
			cv2.imwrite("my_sketch.jpg",sketch(frame))
			break

	#release the camera and close the window
	cap.release()
	cv2.destroyAllWindows()