# Deep Learning Study Tutorial

## Optimization

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/readme_images/optim_gd.png" width="400px"</img> 
</div>

Gradient Descent is a very common scheme of optimization algorithms. It is very useful to find the global/local minimum of the loss function we used to do the training of the model. The most foundmental types of gradient descent methods are the batch gradient descent, mini-batch gradient descent and the stochastic gradient descent. The convergence of these optimization algorithms is proven years ago.

For the deep learning model, the stochastic gradient descent and the mini-batch gradient descent become very popular to train the loss function because they are functional as a kind of regularization to the model complexity. People now use very advanced optimization method based on the stochastiv gradient descent with an adaptive learning rate. Adam is one of the most used optimization algorithm in the deep learning field.

## Convolutional Neural Networks

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/readme_images/cnn_cs231n_nn_vs_cnn.jpeg" width="400px"</img> 
</div>

A convolutional neural network consists of an input and an output layer, as well as multiple hidden layers. The hidden layers of a CNN typically consist of convolutional layers, RELU layer i.e. activation function, pooling layers, fully connected layers and normalization layers.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/readme_images/cnn_structure.png" width="400px"</img> 
</div>

The CNN model is designed to apply an cross-correlation operation (in Math) inspired by the convolution operation into the Nueral Networks' structure. We execute a convolution by sliding the filter over the input. At every location, a matrix multiplication is performed and sums the result onto the feature map. It could help extract the small features of the image rather than summarize the whole image together. More layers or more filters the model has, more specific the extracted features will be. For instance, rather than learn the whole human image together, CNN would extract the nose, eyes, mouth and etc. seperately. However, one disadvatage is that CNN could not extract/recgnize the specific location of the extracted features. Now, a Capsule Network presented by Hinton in 2017 is believed to improve this problem efficiently.

## Autoencoder and VAE(Variational Autoencoder)

### Autoencoder

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/readme_images/ae_structure.png" width="400px"</img> 
</div>

The Autoencoder model is a structure consists of one top-down model and a bottom up model. These two models are called encoder and the decoder. It will compress the information first and then release the information again. 

The basic idea is to use layers of neural networks to encode the original data (images or the sequences) into a low-dimensional vectors of values first. It's like a summarization of the high-dim data by the low-dim data. However, not like PCA, with the neural networks sturcture, the original data would be sent to a high dimensional space first and then to a very low dimensional space.

By using the ConvNet, the decoder layers would be called Deconv layers. It would reconstruct images simlar to the original images. The decoder part could be used as a image generator.

### Variational Autoencoder

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/readme_images/vae_structure.png" width="400px"</img> 
</div>

The VAE is a unsupervised learning method used to generate images similar to the training images. Not like the simple autoencoder model, the VAE tries to learn the distribution of the latent layer from the distribution of the training data and then use the laten layer distribution to learn an approximation distribution to the true distribution. There are several tricks used in the design of the VAE structure and we could explian it in a way of EM algorithm. I will write the detailed derivation later.

## Generative Adversarial Network

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/readme_images/gan_schema.png" width="400px"</img> 
</div>

Not like the VAE, the GAN is a competition between the Generator and the Discriminator. VAE tries to learn a distribution that catches/averages all the modes of the original distribution. However, GAN just want to approximate one mode of the true distribution perfectly. This is one reason that GAN could generate better images. We would want to train the GAN model in seperated steps. First generator would genrate new images and the combined data of generated images and the true images are used to train the discriminator for a binary classification task. Then the discriminator will be frozen, and the generator will be trained in a way of generating fake images with labels saying that these images are real. By iterating these two steps, we could finally have very good fake images.

Record the learning materials for thesis

Week 1: The Overview of Gradient Descent Algorithms with momentum

Week 2 to 3: Introductary Study of CNN

Week 4: How Beautiful are these Animals (Simple application of Convnet, Overfitting not finished yet)

Week 5: AutoEncoder on the Human Face images and Image denoising

Week 6: AutoEncoder-Interpolation

Week 7: Autoencoder with Latent Variable Layer and Variational Autoencoder(VAE)

Week 8-9: Tensorflow Intro for VAE and GAN
