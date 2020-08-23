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
The Next step after finding the gradient is **thnning** via **Non Maximum suppression**. 

Thinning is a type of morphological operation, where given the segmented binary image, you try to reduce it into a series of white pixels connected with each other, rather than clusters connected.
![alt text]()

Non Maximum Suppression or NMS is one of the ways to perform thinning. The basic concept involves comparing the gradient magnitude with its neighbours in the gradient direction or angle.If the pixel value is less than either of the two then it is **suppressed** or assigned 0 pixel value. NMS using interpolation gives much better and acuurate results, but in my code I have not implemented the interpolation. Non maximum suppression without interpolation requires us to divide the 3x3 grid of pixels into 8 sections. Ie. if the gradient direction falls in between the angle -22.5 and 22.5, then we use the pixels that fall between this angle (r and q) as the value to compare with pixel p, see image below.
![alt text]()

**ALGORITHM APPLIED FOR NMS:**
1. We divide the gradient angles in 4 parts or direction, 0deg region (0deg to 22.5 deg or 180 to 157.5) which consists of neighbours in East and West direction, 90deg region(67.5deg to 112.5deg) consisting the neighbours in north and south neighbours, 45deg(22.5deg to 67.5deg) which consists of neighbours in South-East and North-West directions, 135deg(112.5deg to 157.5deg) which consists of neighbours in South-West and North-East directions.
2. Now we find run a loop and check the region of gradient angle of each pixel value. If it lies in 0deg region then the neighbours are, else if in 90deg region then the neighbours are , else if in 45deg region then the neighbours are and if in 135 deg region then the values 




 
 
 











