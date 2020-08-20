# Canny-Edge

Canny edge detector is edge detection operator. It was developed by **John F. Canny** in 1986. 

## **ALGORITHM**

1. First Convert the image into a greyscale image.
2. Then we apply the guassian filter on the image to reduce the noises in the image. If not done then the operator may detect unnecessary edges in the image.
3. Then we find the **Gradient of the image** (both magnitude and direction) using sobel operator. For normalizing the gradient we divide the sobel operators by 8.
