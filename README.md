# DESCRIPTION
Python provides vast libraries which can be used in several fields. Pygame is a crossplatform set of Python modules which can be used to create video games, primarily
2D video games. However, it can be pushed and optimized even further to create 3D
video games. One of the ways, in computer graphics, is to use the Ray Tracing
technique on a smaller scale. Ray Tracing is a technique which is used for rendering
three-dimensional graphics with complex light interactions. In this case, since I am
using Pygame, it can even be combined with a few other algorithms to produce even
better results. I have used the Bresenham’s line algorithm in my project along with
the Ray Tracing algorithm in Pygame to build a 3D video game, by the name of Self
Havoc.   
Similar to the Pygame module, NumPy is a python library which is mainly
used for working with arrays and to perform mathematical operations. I used the
NumPy library to manipulate a given image in the Pygame display window and then
display it in terms of Latin Extended (B) symbols.   
I also used the NumPy module
along with the OpenCV library to further manipulate a complete video in three
different forms and then display it in the Pygame display window. OpenCV is a
library which consists of various programming functions that are mainly aimed at
real-time computer vision.   
My application, GamImiTrack, consists of these three
sub-projects (Self Havoc, Image Manipulation and Video Manipulation) in a single
application. There is still a lot of scope left in this application, primarily in the 3D game,
Self Havoc. It can even further be developed into a shooting or a mission-based 3D
game with multiple stages or levels.

# NOTE
***IMP***  
The main application (GamImiTrack) can be opened by running the 'temp_mainScript.py' script.  

***NOTE-1***  
If you try running the application, you will simply get an error, primarily because of the directory changes (because the directory on my system is different from the directory on your system.)
To run this application on your system, make the appropriate changes in all the scripts mentioned below:

(1) 'FlashArtPy_VideoBnW.py'  
(2) 'FlashArtPy_VideoCol.py'   
(3) 'FlashArtPy_VideoPix.py'  
(4) 'ImageManipulationMain.py'  
(5) 'objects.py'  
(6) 'playerPOV.py'  
(7) 'SelfHavocMain.py'  
(8) 'sprites.py'  
(9) 'temp_mainScript.py'  
(10) 'temp_script.py'    

***NOTE-2***  
Q> What changes do you have to make?  
A> In the scripts, I have loaded various images (textures, sprites, etc.), fonts, music, videos, etc. from the directory on my system, to make use of them in my application.
Now, obviously when you try to run this application on your system, the directory will also be changed.
Simply go to all of the scripts that I have mentioned above, and re-write the directories in those scripts according to your own system and then execute the 'temp_mainScript.py' script.  
If you don't follow these steps, then the scripts will throw an error which will be very similar to 'No such directory found!'.  

The changes to be made are extremely minimal and require almost no effort.  
The application should be good to go inside a minute.  
Have fun!    

# PREVIEW SCREENSHOTS
  
  ***(1) SELF HAVOC (3D GAME)***
  
  ![19BCS2190_o1](https://user-images.githubusercontent.com/79057173/119277193-d22a1e00-bc3b-11eb-95f9-9772b69cfcf3.PNG)

![19BCS2190_o2](https://user-images.githubusercontent.com/79057173/119277194-d35b4b00-bc3b-11eb-8cc5-f7f9dad55399.PNG)

![19BCS2190_o3](https://user-images.githubusercontent.com/79057173/119277196-d5250e80-bc3b-11eb-9880-dd7af6741676.PNG)

![19BCS2190_o4](https://user-images.githubusercontent.com/79057173/119277199-d9512c00-bc3b-11eb-9892-e128da9616bb.PNG)

![19BCS2190_o5](https://user-images.githubusercontent.com/79057173/119277202-da825900-bc3b-11eb-9734-d2148d954f1a.PNG)

![o16_sprites5](https://user-images.githubusercontent.com/79057173/119653919-821ea780-be45-11eb-9810-1c5af564da47.PNG)

![o17_sprites6](https://user-images.githubusercontent.com/79057173/119653926-84810180-be45-11eb-99f8-f59d27e679ef.PNG)

***(2) IMAGE MANIPULATION (LATIN EXTENDED-B SYMBOLS)***

![19BCS2190_o13](https://user-images.githubusercontent.com/79057173/119277260-3cdb5980-bc3c-11eb-87aa-fb3fa59938cf.PNG)

![19BCS2190_o14](https://user-images.githubusercontent.com/79057173/119277261-3ea51d00-bc3c-11eb-8a04-dec582121dbd.PNG)

![19BCS2190_o15](https://user-images.githubusercontent.com/79057173/119277262-3fd64a00-bc3c-11eb-8fd1-08b65f4c0a4e.PNG)

***(3) VIDEO MANIPULATION (3 options: (a) Black and white, (b) Coloured and (c) Custom n-bit pixels***

![19BCS2190_o16](https://user-images.githubusercontent.com/79057173/119277313-888e0300-bc3c-11eb-9178-cee9250a0a65.PNG)

![19BCS2190_o17](https://user-images.githubusercontent.com/79057173/119277317-8a57c680-bc3c-11eb-9de8-a46191f629e9.PNG)

![19BCS2190_o20](https://user-images.githubusercontent.com/79057173/119277318-8c218a00-bc3c-11eb-9121-630330fb4999.PNG)

![19BCS2190_o22](https://user-images.githubusercontent.com/79057173/119277321-8d52b700-bc3c-11eb-89e2-d3c2adfd6c05.PNG)
