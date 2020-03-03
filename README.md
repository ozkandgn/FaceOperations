# FaceOperations
Face Angle &amp; Eye Blinking Detection

In this project, it is aimed to establish an image processing service.

The face, eye, blink and angle of the face on the video were determined.

The service has triggered with video link and video name because of the media is running on the server.

Keras and some image processing opeerations was used for CNN but CNN was not as efficient as dlib.

Binary Transformation:

![](https://github.com/ozkandgn/FaceOperations/blob/master/images/binary.png)

The dlib library was used for face detection and most other processes. Dlib uses HOG(histogram of oriented gradients
) to find face and gives us landmarks.

HOG:

![](https://github.com/ozkandgn/FaceOperations/blob/master/images/hog.png)

Landmarks:

![](https://github.com/ozkandgn/FaceOperations/blob/master/images/dlib.png)

As a result, a blink and face angle detection application was performed on the server.
