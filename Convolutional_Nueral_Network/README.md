# Deep Learning Study Tutorial

## Introductary Study of CNN

In this notebook, the basic construction of the CNN is introduced by coding in Keras. The dataset used here is the Fashion MNIST data which can be considered as a improved version of the handwritten MNIST data for the neural networks study. The Fashion MNIST data contains images of shoes, clothes, pants, ..., 10 in total. We could see how the CNN extract the features of the images by visualizing the filters of each ConvNet layer.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Convolutional_Nueral_Network/readme_images/cnn_fashionmnist_filters1.png" width="400px"</img> 
</div>
<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Convolutional_Nueral_Network/readme_images/cnn_fashionmnist_filters2.png" width="400px"</img> 
</div>
<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Convolutional_Nueral_Network/readme_images/cnn_fashionmnist_filters3.png" width="400px"</img> 
</div>

Here I just plot out 3 examples and each one has 1 filter plotted out for each layer. We could see that as the model goes deeper, more detailed feature is exaggerated.

## CNN Tensorflow with ImageNet data

In this notebook, the CNN model is coded by tensorflow. Though in my mind Keras is much easier to use, Tensorflow would be useful to construct deeper networks. When the Tensorflow 2.0 comes out officially, Keras would be the king.

The classification task for the ImageNet data is done here and I chose the horse image to visualize the filter map of one layer.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Convolutional_Nueral_Network/readme_images/cnn_horse.png" width="200px"</img> 
</div>
<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Convolutional_Nueral_Network/readme_images/cnn_horse_filtermap.png" width="600px"</img> 
</div>

## How Beautiful are these Animales?

This is a project that use CNN to classify the real-life data. The dataset here contains more than 4000 images of animals. Some of the images have high quality and are considered as good photos. However, some other images have low quality and are considered as bad photos. Here are two examples:

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Convolutional_Nueral_Network/readme_images/cnn_animal_good_bad.png" width="600px"</img> 
</div>

The left one is considered good image and the right one is considered not good. The CNN model is built to extract the information from the training images to distinguish the bad quality and the good quality of images.
