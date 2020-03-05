from PIL import ImageGrab, ImageOps 
import pyautogui 
import time 
import numpy as np   
     
class cordinates(): 
    replaybutton =(360, 214) 

def restartGame(): 
    pyautogui.click(cordinates.replaybutton)


def press_space(): 
    pyautogui.keyDown('space') 
    time.sleep(0.05)  
    pyautogui.keyUp('space') 
   
n=2
def imageGrab():  
    box = (174,227,261+n,240)
    image = ImageGrab.grab(box) 
    grayImage = ImageOps.grayscale(image) 
    a = np.array(grayImage.getcolors()) 
    return a.sum() 

restartGame()
time.sleep(0.4)
sum=0       
for i in range(5):   
    sum=sum+imageGrab()     

print(sum/5)

while True:  
    if imageGrab()>sum/5:
        press_space()
#let's run the code!
       