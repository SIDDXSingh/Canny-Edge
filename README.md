# Canny-Edge

Canny edge detector is edge detection operator. It was developed by **John F. Canny** in 1986. 
In my code I have implemented canny edge algorithm from scratch by using **Numpy Library**

## **ALGORITHM For CANNY EDGE DETECTION**

1. First Convert the image into a greyscale image.
2. Then we apply the guassian filter on the image to reduce the noises in the image. If not done then the operator may detect unnecessary edges in the image.
3. Then we find the **Gradient of the image** (both magnitude and direction) using sobel operator. For normalizing the gradient we divide the sobel operators by 4. We can also use **Scharr operator** for convolution.
4. After finding then Gradient we apply **Non Maximum Suppression** on the magnitude which is basically a **Thinning step**.
5. After that we apply **Hysterisis Thresholding.**

## Applying guassian filter and also finding the Gradient of the image using sobel Operator:

We can define a guassian kernel of specific size and convolute it on the image to smooth it. Or we can also use the formula of guassian kernel to generate it based on the size given by the user.

Now, for finding the gradient of smoothed image we use sobel kernel. 
For gradient in x the sobel operator is:
```
[[1, 0, -1],
 [2, 0, -2],
 [1, 0, -1]]
 ```   
For gradient in y the sobel operator is:
 ```
[[1, 2, 1],
 [0, 0, 0],
 [-1, -2, -1]]
 ```
 
 Now we **Convolve the kernel** over the image and get the resultant in both the directions.
Since we are using Numpy here, we can use the **stride tricks** function for faster computation rather than using for *loops* for Convolution. Its is much more faster and efficient than for *loop*.

Now we find the magnitude of the gradient image. Suppose the gradient in x direction is grad_x and gradient in y direction is given by grad_y.The magnitude is given by:
``
np.hypot(grad_x,grad_y)
``
which simply computes the hypothenuse using the *Pythagoras Formula.*

We also need to find the gradient direction for the image. It can be found by using the arctan2 function.
`` np.arctan2(grad_y, grad_x)``

The result we get is in radians. For our convinience we convert our result in degrees.
The range of arctan2 varies from *-180 deg to 180 deg.* Graph for arctan2 is given below.
![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Atan2_argument_sign_graph.svg/750px-Atan2_argument_sign_graph.svg.png)


But for our operations we need angles in the range 0 to 180 degrees. So we add 180 degrees to the gradient angle for all the values which are less than 0.


## Non Maximum Suppression:
The Next step after finding the gradient is **thnning** or **Non Maximum suppression**. 


 
 
 











