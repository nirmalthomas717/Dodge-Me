# Dodge-Me
// An Automated Nerf Turret that can track human faces and orient itself to shoot at them, 
// creating a new Human-Toy Interaction that can stimulate reflex responses from the user. 
// Combining computer vision &amp; physical computing to explore novel ideas of entertainment!

// The codes given are divided into 2 parts. One for the arudino which will be running on the arduino and 
// another for Open CV which will be running on your computer.

// The open CV code needs to be setup after enabling serial communication between the arduino and the computer. 
// Once the code detects the face, it will send instructions to create a red box around the face on the computer screen.
// The computer then send the co-ordinates of the face to the arduino to intiate the servo to centre itself to the face.
// When the position of the face changes, the new co-ordinates are send and this loop continues and once the face is centered,
// the firing mechanism wil be triggered to shoot the nerf bullet.