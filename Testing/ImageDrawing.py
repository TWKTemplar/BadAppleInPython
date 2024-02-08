
import matplotlib.pyplot as plt
import numpy as np
import os
import random
def flood(size):
    # Create folder if it doesn't exist
    if not os.path.exists("Images"):
        os.makedirs("Images")
    grid = np.zeros((size, size))
    count = 0
    for i in range(size*size):
        x = i // size #i is divided by size and floored
        y = i % size #i is divided by size and floored the original value is subtraced and the remainder is = to y
        grid[x, y] = Draw(x, y, grid)
        plt.imshow(grid)
        plt.clim(0, 1)
        plt.savefig(os.path.join("Images", str(count) + ".png"), dpi=50)
        count += 1
def Draw(x ,y ,grid ):
    draw = 0
    if(x >= y):
        draw = 1
    return draw

flood(10)