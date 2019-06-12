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
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Methodology/readme_images/nn_3.png" width="400px"</img> 
</div>

Based on our choice of loss function, we can do gradient descent based algorithms such as stochastic gradient descent with the momentum or the Adam algorithm to train the neural networks.