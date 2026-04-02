'''Module 3: count black and white pixels and compute the percentage of white pixels in a .jpg image and extrapolate points'''


'''
Updated code uses less loops 
Simplifying the process and time it takes for the code to analyze the 6 images 
'''

from termcolor import colored
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import pandas as pd

# Image filenames
filenames = [
    r"C:\Users\Reaga\OneDrive\Desktop\BME_2315\Module-3-Fibrosis\images\MASK_Sk658 Llobe ch010017.jpg",
    r"C:\Users\Reaga\OneDrive\Desktop\BME_2315\Module-3-Fibrosis\images\MASK_Sk658 Llobe ch010018.jpg",
    r"C:\Users\Reaga\OneDrive\Desktop\BME_2315\Module-3-Fibrosis\images\MASK_Sk658 Llobe ch010019.jpg",
    r"C:\Users\Reaga\OneDrive\Desktop\BME_2315\Module-3-Fibrosis\images\MASK_Sk658 Llobe ch010021.jpg",
    r"C:\Users\Reaga\OneDrive\Desktop\BME_2315\Module-3-Fibrosis\images\MASK_Sk658 Llobe ch010022.jpg",
    r"C:\Users\Reaga\OneDrive\Desktop\BME_2315\Module-3-Fibrosis\images\MASK_Sk658 Llobe ch010023.jpg",
]

# Depths (microns)
depths = [15, 30, 45, 55, 60, 80]

white_counts = []
black_counts = []
white_percents = []

print(colored("Counts of pixels by color in each image", "yellow"))

for filename, depth in zip(filenames, depths):

    # Load image in grayscale
    img = cv2.imread(filename, 0)

    # Binary threshold
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Pixel counts
    white = np.count_nonzero(binary)
    total = binary.size
    black = total - white

    # Percent white
    white_percent = 100 * white / total

    # Store values
    white_counts.append(white)
    black_counts.append(black)
    white_percents.append(white_percent)

    # Print results
    print(colored(f"{filename}:", "red"))
    print(colored(f"White pixels: {white}", "white"))
    print(colored(f"Black pixels: {black}", "blue"))
    print(f"{white_percent:.2f}% White | Depth: {depth} microns\n")

# Save results to CSV
df = pd.DataFrame({
    "Filename": filenames,
    "Depth (microns)": depths,
    "White Percent": white_percents
})

df.to_csv("Percent_White_Pixels.csv", index=False)

print("CSV file 'Percent_White_Pixels.csv' created.")


'''the .csv writing subroutine ends here'''


#############
### LECTURE 2: UNCOMMENT BELOW

# Interpolate a point: given a depth, find the corresponding white pixel percentage
<<<<<<< HEAD

interpolate_depth = float(input(colored(
    "Enter the depth at which you want to interpolate a point (in microns): ", "yellow")))

x = depths
y = white_percents

# You can also use 'quadratic', 'cubic', etc.
i = interp1d(x, y, kind='linear')
interpolate_point = i(interpolate_depth)
print(colored(f'The interpolated point is at the x-coordinate {interpolate_depth} and y-coordinate {interpolate_point}.', "green"))

depths_i = depths[:]
depths_i.append(interpolate_depth)
white_percents_i = white_percents[:]
white_percents_i.append(interpolate_point)


# make two plots: one that doesn't contain the interpolated point, just the data calculated from your images, and one that also contains the interpolated point (shown in red)
fig, axs = plt.subplots(2, 1)

axs[0].scatter(depths, white_percents, marker='o', linestyle='-', color='blue')
axs[0].set_title('Plot of depth of image vs percentage white pixels')
axs[0].set_xlabel('depth of image (in microns)')
axs[0].set_ylabel('white pixels as a percentage of total pixels')
axs[0].grid(True)


axs[1].scatter(depths_i, white_percents_i, marker='o',linestyle='-', color='blue')
axs[1].set_title('Plot of depth of image vs percentage white pixels with interpolated point (in red)')
axs[1].set_xlabel('depth of image (in microns)')
axs[1].set_ylabel('white pixels as a percentage of total pixels')
axs[1].grid(True)
axs[1].scatter(depths_i[len(depths_i)-1], white_percents_i[len(white_percents_i)-1],
               color='red', s=100, label='Highlighted point')


# Adjust layout to prevent overlap
plt.tight_layout()
plt.show(block=True)
=======



interpolate_depth = float(input(colored(
    "Enter the depth at which you want to interpolate a point (in microns): ", "yellow")))

x = depths
y = white_percents

# You can also use 'quadratic', 'cubic', etc. Tell python whatever you need
i = interp1d(x, y, kind='')
i = bary
interpolate_point = i(interpolate_depth)
print(colored(
    f'The interpolated point is at the x-coordinate {interpolate_depth} and y-coordinate {interpolate_point}.', "green"))

depths_i = depths[:]
depths_i.append(interpolate_depth)
white_percents_i = white_percents[:]
white_percents_i.append(interpolate_point)


# make two plots: one that doesn't contain the interpolated point, just the data calculated from your images, and one that also contains the interpolated point (shown in red)
fig, axs = plt.subplots(2, 1)

axs[0].scatter(depths, white_percents, marker='o', linestyle='-', color='blue')
axs[0].set_title('Plot of depth of image vs percentage white pixels')
axs[0].set_xlabel('depth of image (in microns)')
axs[0].set_ylabel('white pixels as a % of total pixels')
axs[0].grid(True)


axs[1].scatter(depths_i, white_percents_i, marker='o',
               linestyle='-', color='blue')
axs[1].set_title(
    'Plot of depth of image vs percentage white pixels with interpolated point (in red)')
axs[1].set_xlabel('depth of image (in microns)')
axs[1].set_ylabel('white pixels as a % of total pixels')
axs[1].grid(True)
axs[1].scatter(depths_i[len(depths_i)-1], white_percents_i[len(white_percents_i)-1],
               color='red', s=100, label='Highlighted point')


# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()
print('fin')
>>>>>>> origin/Daniel,-Tomas_M3
