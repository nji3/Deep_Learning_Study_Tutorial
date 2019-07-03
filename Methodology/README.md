# Popular Deep Learning Methods Methodology

## Background

Why neural networks based deep learning or machine learning methods are so powerful of dealing with different kinds of difficult tasks these days? One simple explanation is that the structure of neural networks can be considered as a very high-dimensional nonlinear function that gives a great performance in approximating the real relationship behind the data. We can call the basis of deep neural networks as deep feedforward networks, feedforward neural networks or multilayer perceptrons. And a full forward structure of neural networks is represented below:

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Methodology/readme_images/nn_1.png" width="400px"</img> 
</div>

The dimension of each hidden layer is usually designed by ourself. However, when using neural networks, we need to match the dimensions of the input and the output data. Because of the multilayer structure, neural networks have super-high dimensionality, which makes it hard to calculate the parameters for each layer. The breakthrough is the back-propagating methods. Based on these back-forward derivatives, the gradient descent based algorithms can be applied to update the loss function step by step. Let’s see the back-propagation presentation.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Methodology/readme_images/nn_2.png" width="400px"</img> 
</div>

Each stage of this process consists of two parts: derivation on the hidden layer and the derivation on the parameters for each layer. The derivations can be shown by two formulas.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Methodology/readme_images/nn_3.png" width="200px"</img> 
</div>

Based on our choice of loss function, we can do gradient descent based algorithms such as stochastic gradient descent with the momentum or the Adam algorithm to train the neural networks.

## Supervised Learning Models

### Convolution Neural Networks

The deep learning book chapter 9 gives a thorough introduction of the convolutional networks. This chapter starts with the convolution operation that contains the multidimensional array of input data and the multidimensional array of parameters as kernel implementing the infinite summation as a summation over a finite number of array elements. We can use a two-dimensional kernel K for a two-dimensional input image I to show a convolution operation:

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Methodology/readme_images/cnn_1.png" width="400px"</img> 
</div>

In addition, the convolution operation is commutative and the commutative formula is im- plemented more straightforward because of less variation in the range of valid values of m and n. The commutative formula is shown below.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Methodology/readme_images/cnn_2.png" width="400px"</img> 
</div>

We could see that we could choose the values for m and n based on the dimensionality of the input image. Based on the design of the convolution, it is not necessary to do linear operations on the whole image directly but select small regions of the image to condense and detect the patterns. As the kernel moves around the image, different kinds of patterns would be detected based on the specific kernel we use. For example, if we have a 3 x 3 kernel with only one row of 1 and other indices equal to 0, this kernel would detect a short horizontal bar in the image. And these patterns will be stored in various filters. The total number of filters can be chosen by our design, just like the dimension increasing for the hidden layers in the forward neural networks.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Methodology/readme_images/conv_one_layer.jpeg" width="200px"</img>
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Methodology/readme_images/conv_one_layer_neuron_model.jpeg" width="200px"</img>  
</div>

The above are two pictures from the Stanford CS231 note. The left one shows an example of neurons in one Convolutional layer for a CIFAR-10 image. We could see that according to the kernel, we could store the pattern into a filter with different dimension. Here, the next layer filter contains five neurons. The right figure shows that the neuron is still as same as what we have in a normal forward neural network with a dot product of the weights and the input. However, the difference is that this time the input restricted to be local spatially because of the connectivity caused by the kernel.

When coding for the convolution networks, there are two more important parameters. We need to specify the ?stride? and the size of the zero-padding. The stride determines the number of pixels that the filter slides. If stride is 1, then the filter will slide one pixel at a time. The zero-padding is used to pad the input volume with zeros around the border so that it would be easier to control the size of the output volumes. According to the CS231 note, we could use a function to calculate the size of the output volume:

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Methodology/readme_images/cnn_3.png" width="200px"</img> 
</div>

W is the input volume size, F is the size of the filter in the receptive field size, S is the stride and P is the amount of zero-padding used on the border. Only If the result is an integer, we could consider the output size would be a fit or valid. For instance, a 7 x 7 input and a 3x3 filter with stride1and pad0 will give a 5x5 output. After one layer of the convolution network, we could add a pooling layer to stabilize the extracted pattern and an activation layer to reduce the activated neurons. It all depends on how we are going to design the structure.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Methodology/readme_images/cnn_structure.png" width="400px"</img> 
</div>
