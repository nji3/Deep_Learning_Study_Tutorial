# Generative Adversarial Networks

## GAN MNIST Tensorflow

This notebook is a implementation of the GAN model on the MNIST data in tensorflow. I did not wrote the whole training model into a class so that it could be easy for people to debug and modify. Because the MNIST data is very simple, I only use a very shallow GAN model here and the dimension of the latent input for the generator is only 20. The result is still good enough. Just remeber to use GPU to train the model for fast speed.

The training losses of the discriminator and the generator are shown below. Also the generated handwritten digits images are show here.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Generative%20Adversarial%20Network/readme_images/gan_mnist_loss.png" width="400px"</img>
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Generative%20Adversarial%20Network/readme_images/gan_mnist.png" width="400px"</img>
</div>

## GAN KERAS

This notebook contains a Keras implementation of DCGAN training on all the car images data in CIFAR10. All these images are compressed to be 32x32x3 so that it would be easier for training. Below is a sample of the original compressed images.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Generative%20Adversarial%20Network/readme_images/GAN_Keras_1.png" width="400px"</img>
</div>

One very important thing is trick we need to know is that, during the training, if the discriminator loss decreases fast to 0 and the adversarial loss increases hugely, it might mean the discriminator was too well trained and control the whole model. When you meet such a situation, you could try too decrease the learning rate for the discriminator to slow it down.

My training model here randomly sample 20 images from the training set to train the model in each step. It's not like what we usually do to go over the whole data set by small batches. It depends on your own design. Here I only did 20000 steps. More steps might give better generated images.

The result is here:

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Generative%20Adversarial%20Network/readme_images/GAN_Keras_2.png" width="800px"</img>
</div>
