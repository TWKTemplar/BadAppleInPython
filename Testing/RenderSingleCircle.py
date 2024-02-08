from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import random
import math
def Render(imgpath):

    # Get Data
    img = Image.open(imgpath)
    #pixel_data = list(img.getdata())
    imgWidth = img.width
    imgHeight = img.height
    # Make Image
    grid = np.zeros((imgHeight,imgWidth))
    for y in range(imgWidth):#left n right
        for x in range(imgHeight):# up and down
            grid[x, y] = IsInCircle(x,y, imgHeight*0.5, imgHeight*0.5, imgHeight*0.1)
    SaveImage(grid)
def ran(num,maxnum):
    if(int(num) > random.randint(0,int(maxnum))):
        return 1
    return 0
def IsInCircle(x,y, Cx, Cy, radius):
    dist = math.sqrt(  ((Cx-x)*(Cx-x)) + ((Cy-y)*(Cy-y))  )
    if(dist < (radius + random.randrange(0,int(radius*1.2)))):
        return 1

    return 0

def SaveImage(grid):
    plt.imshow(grid)
    plt.clim(0, 1)
    if not os.path.exists("Render"):
        os.makedirs("Render")
    plt.savefig(os.path.join("Render", "apple" + ".png"), dpi=50)
def GetSourceImagePath():
    if not os.path.exists("BadApple"):
        os.makedirs("BadApple")
    imageFolder = "BadApple"
    imageName = "BadApple0086"
    imagePath = os.path.join(imageFolder, imageName + ".png")
    return imagePath
Render(GetSourceImagePath())