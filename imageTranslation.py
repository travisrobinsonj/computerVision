from argparse import ArgumentParser
import cv2
import numpy as np

#get arguments
def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--xratio')
    parser.add_argument('--yratio')
    parser.add_argument('--image')
    return parser


if __name__ == '__main__':
	parser = get_parser()
	args = parser.parse_args()
	image = cv2.imread(args.image)

	#store height and weight of the image
	height , width = image.shape[:2]
	trans_height, trans_width = height/float(args.yratio), width/float(args.xratio)
	# T is  our translation matrix
	T = np.float32([[1,0,trans_width],[0,1,trans_height]])

	#we use warpAffine to transform the image using the matrix T
	img_translation = cv2.warpAffine(image,T,(width,height))
	cv2.imshow('Translation',img_translation)
	cv2.imwrite('./images/translation_image.png',img_translation)
	cv2.waitKey()
	cv2.destroyAllWindows()

