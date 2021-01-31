import cv2
import numpy as np
import math

# I found some of the code i am using over here ath this web page.
# https://github.com/aydal/Cylinderical-Anamorphosis/blob/master/anamorph.py
# I found the above formentioned web page, when I found the one below.
# I found the one below, by typing "opencv python animorphic"
# into a google web search.
# https://stackoverflow.com/questions/54271864/anamorphosis-in-python


slider1_max = 20
slider1_min = 1
title_window = 'Window Title Goes Here'
trackbar1_name = 'Inner Dia'
global val
val = 0

cv2.namedWindow(title_window)
img = cv2.imread("catHead.jpg")
#cv2.imshow("Original Picture",img)

def percent_scale(src,percentageToScaleBy):
    oh,ow = src.shape[:2] # get shape information
    scale = percentageToScaleBy 
    scaleW = int(ow * (scale / 100)) # scale width by percentage
    scaleH = int(oh * (scale / 100)) # scale Height by percentage
    src = cv2.resize(src,(scaleW,scaleH), interpolation = cv2.INTER_AREA)
    #cv2.imshow("Scaled Picture",src)
    return src


def on_Irad(thisVal):
    global val
    val = thisVal
    Irad = val
    arc = arch_Image(img,Irad)
    update_image(arc)


def update_image(src):
    cv2.imshow(title_window,src)


def convt(R,b,c):
        q = int(math.trunc((b*cols/(2*math.asin(1)))))
        p = int(math.trunc(c-R))
        result = (q,p)
        return result

        
def arch_Image(sourceImage,innerRadius,offset = True):
        modifier = 10
        innerRadius = innerRadius * modifier
        innerDiameter =  innerRadius*2 
        c = int(innerRadius + rows) 
        # make a new blank image to place the freshly created warped image into
        # with enough room for placing a cylinderical object to project onto.
        if offset == False:
                imageCylinderPlaceHolderOffset = 0
        else:
                imageCylinderPlaceHolderOffset = innerRadius
        
        blank = np.zeros([int(c + imageCylinderPlaceHolderOffset),2*c,3],dtype = np.uint8)
        blank.fill(0)
            
        for i in range (0,2*c):
                for j in range (1,c):
                        b = math.atan2(j,i-c)
                        R = math.sqrt(j * j + math.pow(i - c, 2))
                        
                        if R >= innerRadius and R <= c:
                                (q,p) = convt(R,b,c)
                                blank[c-j,i-1] = sourceImage[p-1,q-1]
        return blank
        

    
img = percent_scale(img,25) #scale original image by a set percentage
cv2.imshow("Scaled Picture",img)

# other variables
(rows,cols) = img.shape[:2]
Irad = 5


cv2.createTrackbar(trackbar1_name, title_window, slider1_min, slider1_max, on_Irad)


# Show some stuff
on_Irad(slider1_min)


print("Please makesure that your source image is in")
print("the same directory that ")
print("this 'Adjustable Arc Image Converter 1.py' file is in")
print("this will help eliminate alot of problems.")
print(" ")
print("Press the 's' key to save your output.")
print(" ")
saveTitle = "arc1.jpg"
print("The current save file name to be is:",saveTitle)


# make it possible to save the output
finish = False
while not finish:
    key = cv2.waitKey(0)
    if key == ord('s') or key == ord('S'):
        #print("val = ",val)
        Irad = val
        arc = arch_Image(img,Irad)
        cv2.imwrite(saveTitle,arc)
        print("Saved image:",saveTitle)
    elif key == 27:
        finish = True
