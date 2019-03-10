# Generative Adversarial Networks

## GAN MNIST Tensorflow

This notebook is a implementation of the GAN model on the MNIST data in tensorflow. I did not wrote the whole training model into a class so that it could be easy for people to debug and modify. Because the MNIST data is very simple, I only use a very shallow GAN model here and the dimension of the latent input for the generator is only 20. The result is still good enough. Just remeber to use GPU to train the model for fast speed.

The training losses of the discriminator and the generator are shown below. Also the generated handwritten digits images are show here.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Generative%20Adversarial%20Network/readme_images/gan_mnist_loss.png" width="400px"</img>
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Generative%20Adversarial%20Network/readme_images/gan_mnist.png" width="400px"</img>
</div>
