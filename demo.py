from SimpleCV import Camera,Display
import time
cam=Camera() # //Intializing camera
time.sleep(5) #//delay for three seconds
a=cam.getImage()#//capturing the first image
a.save("a.jpg")
time.sleep(1






















           ,
           0)
b=cam.getImage()#//capturing the second image after one second
b.save("b.jpg")
d=b-a #//subtracting the image pixels
#d.show() #// display the subtracted image
mat=d.getNumpy() #//converting to numpy array
avg=mat.mean() #//take the mean
print avg #//print average value on the screen
if avg>6:
    print("Motion Detected")
else:
    print("not detected")