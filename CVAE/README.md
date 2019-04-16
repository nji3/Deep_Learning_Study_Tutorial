# Conditional Variational Autoencoder

## Conditional Variational Autoencoder MNIST

### Condition on the labels

In this notebook, I compare the result of MNIST digits reconstruction and generating by VAE model and the CVAE model conditioning on the labels of the digits (0 to 9).

The CVAE model I used here has a one layer deeper fully connected model than the VAE model I used. However, the CVAE model is still a little better than the VAE in the reconstruction.

VAE reconstruction sample:

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/CVAE/readme_image/VAE_fc_recon_sample.png" width="600px"</img> 
</div>

CVAE reconstruction sample:

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/CVAE/readme_image/CVAE_label_recon_sample.png" width="600px"</img> 
</div>

When it comes to the generator, things get very worse in VAE model.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/CVAE/readme_image/VAE_recon_fail.png" width="400px"</img>
</div>

A great disadvantage of the VAE model is that it is very hard to control the normal distributions we learnt to produce the specific images we want. However, CVAE shows its advantage here. By sending the one hot vector indicating the labels of digits, the neural network learns a normal distribution for each group of the digits. When we want to generate digits in one group, we just specific the one hot vector of that group for decoding.

Here are some samples of the generated digits for each label.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/CVAE/readme_image/CVAE_labels.png" width="400px"</img> 
</div>

### Condition on the missing part of the images

In this notebook, I worked on a different task that fill the missing part of the images by applying the CVAE model conditioning on the missing part.

The model constructed here is as same as the one I used above for the labels. I removed a middle 10 by 10 square in one image. we could take a look of a sample below.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/CVAE/readme_image/CVAE_imp_full_flaw.png" width="400px"</img>
</div>

I did not do a very thourgh training and the model tuning for this task. I think the result is still okay. At least we could see that CVAE conditioning on the missing part actaully works for the image impainting task.

The reconstruction result for the training image (From top to below is Flawed images, Reconstructed images, Original images):

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/CVAE/readme_image/CVAE_imp_train.png" width="600px"</img>
</div>

The reconstruction result for the testing image (From top to below is Flawed images, Reconstructed images, Original images):

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/CVAE/readme_image/CVAE_imp_test.png" width="600px"</img>
</div>
