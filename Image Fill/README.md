# Image Fill

The dataset I used here is just the CIFAR10 data with the designed missing part in the image.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Image Fill/readme_image/car_incomp_exp.png" width="600px"</img> 
</div>

## Image Fill by Direct Convolution

Let's start with a very simple and direct way for the image filling. The input data is a four channel incompleted image with a fourth channel indicating the missing part of the image.

A four-layer Convolution Nueral Network model is built here. Each layer has 64 channels with a 5x5 kernel size. The final result will be a filled-in 3-channel image.

By limited training process, we could take a look at the result for the training images and the testing images.

Training images filled:

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Image Fill/readme_image/car_conv_fill_train.png" width="600px"</img> 
</div>

Testing images filled:

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Image Fill/readme_image/car_conv_fill_test.png" width="600px"</img> 
</div>

The reconstruction can give a reasonable fill-in but still very blur. It generally just fill in the colors by the nearby color patterns but it cannot give a very good reconstruction for some detailed small missing patterns like the rear mirrows or the car boundaries.
