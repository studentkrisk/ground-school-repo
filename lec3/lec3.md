Covering: YOLO, blob detection

# Blob Detection
- can be used to detect objects if background is uniform

## Laplacian of Gaussian (2 Steps)
1. applies gaussian blur
	- preprocessing step
	- reduces noise for laplacian step
	- convolution with gaussian kernel (1 2 1 / 2 4 2 / 1 2 1) * 1/16
2. applies laplacian operator
	- takes the second order derivative in each direction
	- detects edges
	- can be approximated by a kernel

### Convolutions
- applies kernel function to entire matrix by scanning it across
- will result in a smaller matrix
- kernel is applied to each pixel
- used for efficient gaussian blurring


## OpenCV SimpleBlobDetector
different approach! starts with thresholding and grouping
1. convert RGB to grayscale
2. mask picture based on whether or not the pixel is brighter than the threshold or not
3. merge nearby pixels into blobs and filter blobs that do not reach certain criteria

# YOLO

## ML
- based on biological neurons
- activation is based on weights and biases of input nodes
- to determine most similar, use dot product
- apply softmax to convert to probability
- using hidden layers allows for nonlinear seperation
- common activation functions: sigmoid, tanh, relu
	- relu is my favourite!!!
- during epochs, we update weights and biases
- these are learned through minimizing a loss function
- gradient descent
	- learning rate is how much you move during gradient descent
- methods to prevent getting stuck in a local minimum
	- simulated annealing!!!
	- random restarts
- it's proven that any function can be modeled by a neural network
- to make a neural network better
	1. add more layers/inputs/neurons
	2. train with more data
	3. get clever
		1. add convolutions
		2. add pooling

## YOLO: One Shot CNN
- two-shot
	- two passes
	- first shot proposes object locations
	- more accurate but slower
- one-shot
	- one pass of the input image

## YOLO architecture
- convolution layers
- pooling
- ReLU
- train/validation/test
	- generally, 70/20/10 split
	- training data = data that changes weights
	- validation data = tunes metaparameters
	- test data = just used to test how good the model is
- overfitting
	- better matches the points but works worse on test data