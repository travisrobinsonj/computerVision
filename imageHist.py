"""
Visualizing color component of an image
"""
import cv2
import matplotlib.pyplot as plt
from argparse import ArgumentParser

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--image')
    return parser
def plotImage(image):
	"""
	  imput image and return histogram distribution of the color
	"""
	img = cv2.imread(image)
	color = ('b', 'g', 'r')
	for i, col in enumerate(color):
		hist2 =cv2.calcHist([img],[i],None,[256],[0,256])
		plt.plot(hist2, color=col, label=col)
		plt.xlim([0,256])
		plt.legend()
	plt.savefig("histogram1.png")
	plt.show()
	
def plotRavImage(image):
	img = cv2.imread(image)
	hist1 = cv2.calcHist([img],[0],None,[256],[0,256])
	#plot the histogram, ravel() flatten image array
	plt.hist(img.ravel(), 256,[0,256])
	plt.savefig('histogram2.png')
	plt.show()


if __name__ == '__main__':
	parser = get_parser()
	args = parser.parse_args()
	plotImage(args.image)
	plotRavImage(args.image)

