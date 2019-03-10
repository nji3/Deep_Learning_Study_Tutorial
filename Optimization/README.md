# Optimization

## Gradient Descent

In the jupyter notebook file, I simulate the data and tried the batch gradient descent, stochastic gradient descent and the mini-batch gradient dscent for the mean squared loss. By tracking each of these optimization algorithms on the contour plots, we could see the difference.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Optimization/readme_images/gd_3plots.png" width="600px"</img> 
</div>

Gnerally the batch gradient descent and the mini-batch gradient descent just stick to the direction of the gradient. And we know that the mini-batch gradient descent would consume much less time. The stochastic gradient descent moved with much more variance, which make it not as stable as the other two.

## Momentum

Momentum is a definition from the physics. The idea is to give the gradient pursuing method a boost from a direction other than the gradient direction so that it could jump out of the local minimum and continue to minimize the loss function. We know that the stochastic gradient descent is very easy to be trapped in the local minimum. With the momentum, it could work better.

<div align="center">
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Optimization/readme_images/gd_womom.png" width="400px"</img> 
        <img src="https://github.com/nji3/Deep_Learning_Study_Tutorial/blob/master/Optimization/readme_images/gd_wmom.png" width="400px"</img> 
</div>

The image at left is the SGD without the momentum and the image at right is the SGD with the momentum. When the SGD trapped in the local minimum, the gradient goes to zero and it is just stuck there. With the momentum, it could jump out of the saddle point and continue go to the real global minimum.
