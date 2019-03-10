# Autoencoder and Variational Autoencoder

## Autoencoder

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Autoencoder_and_VAE/readme_images/ae_f_m.png" width="200px"</img> 
</div>

The autoencoder notebook used the human face images consist of 131 images, 49 men, 20 women, usually a neutral and smile of each, collected at the European Conference on Visual Perception in Utrecht, 2008. The original resolution is 900x1200 and in the notebook i transfered all the images to 128x128 for the training convinience. Above are two sample images of the training data.

Before the autoencoder model, we could visualize the PCA eigen faces of the training images. Actually very shallow autoencoder model just works like a approximation of the PCA. The PCA works best in the grey images and here I just used the black channel of the training images.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Autoencoder_and_VAE/readme_images/ae_pca.png" width="400px"</img> 
</div>

Two autoencoder models are built here. One model is used to train the black channel of the images and another model is used to train all three channels of the images. Both networks are built in Keras and you could see the detailed summary in the notebook. We can see the performance of the reconstruction for the test images below.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Autoencoder_and_VAE/readme_images/ae_1c_recon_test.png" width="400px"</img> 
</div>

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Autoencoder_and_VAE/readme_images/ae_3c_recon_test.png" width="400px"</img> 
</div>

Autoencoder model can also be used as a efficient tool to do denoising task. The noise in the images or the sequences can be filtered out during the training process. The most important features and the information would be retained during encoding and the noise would be deactivated to 0 and disappear. I added some noise into the face images from a normal distribution and we could check the performance of the denoising below.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Autoencoder_and_VAE/readme_images/ae_1c_denoise.png" width="400px"</img> 
</div>

### Autoencoder Interpolation

Autoencoder model with latent layer (which is a fully connected layer after the ConvNets) could do a image shifting process called the Interpolation. In this notebook, I trained the autoencoder model on both the MNIST handwritten data and the ECVPU face images. To do the interpolation, just choose the two images you want and find out the vetors respect to these two images in the latent layer. And then we could calculate the difference between these two vectors and linearly seperate them evenly by a selected number of steps. When we put all these step vectors into the generator, we could visualize how one image shifts to another one.

Here are the Interpolation examples for the MNIST data:

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Autoencoder_and_VAE/readme_images/ae_mnist_ip1.png" width="400px"</img> 
</div>
<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Autoencoder_and_VAE/readme_images/ae_mnist_ip2.png" width="400px"</img> 
</div>
<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Autoencoder_and_VAE/readme_images/ae_mnist_ip3.png" width="400px"</img> 
</div>

Here are the Interpolation examples for the Face images:

Male transfer to male

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Autoencoder_and_VAE/readme_images/ae_face_ipm.png" width="400px"</img> 
</div>

Female transfer to female

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Autoencoder_and_VAE/readme_images/ae_face_ipf.png" width="400px"</img> 
</div>

Male transfer to female

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Autoencoder_and_VAE/readme_images/ae_face_ipmf.png" width="400px"</img> 
</div>

## Variational Autoencoder (VAE)

###
