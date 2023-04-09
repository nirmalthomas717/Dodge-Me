# Dodge-Me
An Automated Nerf Turret that can track human faces and orient itself to shoot at them, creating a new Human-Toy Interaction that can stimulate reflex responses from the user. Combining computer vision &amp; physical computing to explore novel ideas of entertainment!

The code is divided into 2 parts. Part 1 Arduino Code and Part 2 Python OpenCV Code.
Arduino needs to be communicating the xy values of the servo motors throught serial communication to the open cv and vice versa.
The open CV code allows you to connect a camera to the toy interface and detect and enclose a red rectangle on the screen once a face is within the view of the camera.
Once the camera detect a face, the co-ordinates of the face is sent to the arduino to reorient itself in a way that the face is in the centre of the screen. Once this is achieved, the trigeering mechanism is activated and the gun shoots the nerf bullet at the target person.
