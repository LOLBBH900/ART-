"Images_04_Grayscale_and_Color_Trackbars"
# Connor Henkes, Engineer Your World
# Created in September 2024, last updated in Sep 2024
# Read in an image file, convert it to grayscale, identify "light" and "dark"
# regions of the grayscale image, and color each region with a different
# color. Allow grayscale division and colors of papers to be adjusted using
# trackbars. Display original, grayscale, colored parts, and customized image.
# Save results if desired. Destroy all windows when user has finished.

# Import libraries
import cv2
import numpy
import os.path
import json

# Function to save the color scheme with stringified keys
def save_color_scheme(current_color_scheme, file_path="color_scheme.json"):
    # Convert tuple keys to strings
    color_scheme_to_save = {str(k): v for k, v in current_color_scheme.items()}
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(color_scheme_to_save, file)
        print(f"Color scheme saved to {file_path}.")
    except Exception as e:
        print(f"An error occurred while saving the color scheme: {e}")
        
# Function to load a saved color scheme
def load_color_scheme(file_path="color_scheme.json"):
    if not os.path.exists(file_path):
        print(f"No saved color scheme found at {file_path}.")
        return None
    with open(file_path, 'r', encoding='utf-8') as file:
        loaded_color_scheme = json.load(file)
    print(f"Color scheme loaded from {file_path}.")
    return loaded_color_scheme

# Initialize 'image' before it's being used
image = None

# Function to apply the loaded color scheme to the image
# Rename 'image' to 'processed_image' inside apply_color_scheme function
def apply_color_scheme(image_local, loaded_color_scheme):
    # Check if loaded_color_scheme is None before proceeding
    if loaded_color_scheme is None:
        raise ValueError("Loaded color scheme is None. Please check if the color scheme was loaded correctly.")
    
    # Apply color scheme
    for (lower, upper), color in loaded_color_scheme.items():
        mask = cv2.inRange(image_local, lower, upper)  # Use 'image_local' inside the function
        image_local[mask != 0] = color
    
    return image_local

# Inside your main image processing logic

# Ask if the user wants to load a saved color scheme
load_choice = input("Would you like to load a saved color scheme? (y/n): ")
if load_choice.lower() == 'y':
    color_scheme_loaded = load_color_scheme()
    
    # Check if the color scheme was loaded correctly
    if color_scheme_loaded is None:
        print("No valid color scheme found. Continuing without loading.")
    else:
        if image is None:
            print("No image loaded yet.")
        else:
            try:
                image = apply_color_scheme(image, color_scheme_loaded)
                print("Color scheme applied successfully.")
            except Exception as load_error:  # Changed exception variable name from 'e' to 'load_error'
                print(f"Error applying color scheme: {load_error}")

# Initialize the color scheme to avoid "used-before-def" error
color_scheme = {
    (0, 50): [255, 0, 0],  # Example entries for color scheme
    (51, 100): [0, 255, 0],
    (101, 150): [0, 0, 255]
}

# After adjusting the color scheme with trackbars, ask if the user wants to save it
save_choice = input("Would you like to save the current color scheme? (y/n): ")
if save_choice.lower() == 'y':
    if not color_scheme:  # Check if the color scheme exists before saving
        print("No color scheme to save.")
    else:
        try:
            save_color_scheme(color_scheme)
        except Exception as save_error:  # Changed exception variable name from 'e' to 'save_error'
            print(f"Error saving color scheme: {save_error}")

# Prompt user to enter name of original image.
import tkinter as tk
from tkinter import filedialog

print("Select your original image using the dialog box.")
root = tk.Tk()
root.withdraw()  # Hide the main window
filename = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg *.jpeg *.png")])

if not filename:
    print("No file was selected. Please try again.")
    filename_valid = False
else:
    filename_valid = True

# Function to stack windows horizontally or vertically
def stack_windows(window_names, direction='horizontal', base_x=0, base_y=0, window_width=400, window_height=300):
    x_offset = base_x
    y_offset = base_y

    for idx, window_name in enumerate(window_names):
        cv2.resizeWindow(window_name, window_width, window_height)
        cv2.moveWindow(window_name, x_offset, y_offset)

        if direction == 'horizontal':
            x_offset += window_width  # Move next window to the right
        elif direction == 'vertical':
            y_offset += window_height  # Move next window below

# Save original image. Create and save grayscale image, ensuring that it
# has the right number of color channels (3).
original_image = cv2.imread(filename, 1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

## Create windows for display.
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Grayscale Trackbars')
cv2.namedWindow('Color01 Trackbars')
cv2.namedWindow('Color02 Trackbars')
cv2.namedWindow('Color03 Trackbars')
cv2.namedWindow('Color04 Trackbars')
cv2.namedWindow('Color05 Trackbars')
cv2.namedWindow('Color06 Trackbars')
cv2.namedWindow('Color07 Trackbars')
cv2.namedWindow('Color08 Trackbars')
cv2.namedWindow('Color09 Trackbars')
cv2.namedWindow('Color10 Trackbars')
cv2.namedWindow('Color01 Parts of Image')
cv2.namedWindow('Color02 Parts of Image')
cv2.namedWindow('Color03 Parts of Image')
cv2.namedWindow('Color04 Parts of Image')
cv2.namedWindow('Color05 Parts of Image')
cv2.namedWindow('Color06 Parts of Image')
cv2.namedWindow('Color07 Parts of Image')
cv2.namedWindow('Color08 Parts of Image')
cv2.namedWindow('Color09 Parts of Image')
cv2.namedWindow('Color10 Parts of Image')
cv2.namedWindow('Customized Image')

# Stack the windows horizontally or vertically
window_names = [
    'Original Image', 'Grayscale Image', 'Grayscale Trackbars',
    'Color01 Trackbars', 'Color02 Trackbars', 'Color03 Trackbars', 
    'Color04 Trackbars', 'Color05 Trackbars', 'Color06 Trackbars',
    'Color07 Trackbars', 'Color08 Trackbars', 'Color09 Trackbars', 
    'Color10 Trackbars', 'Color01 Parts of Image', 'Color02 Parts of Image',
    'Color03 Parts of Image', 'Color04 Parts of Image', 'Color05 Parts of Image', 
    'Color06 Parts of Image', 'Color07 Parts of Image', 'Color08 Parts of Image', 
    'Color09 Parts of Image', 'Color10 Parts of Image', 'Customized Image'
]

# Prompt user for stacking direction
stacking_direction = input("How would you like to stack the windows? ('horizontal' or 'vertical'): ").lower()
stack_windows(window_names, direction=stacking_direction)

# Display original and grayscale images.
cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image', grayscale_image)

# Create variable to read in the height, width, and number of channels (3) of
# the original image.
image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

# Create the colored papers.
Color01_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)
Color02_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)
Color03_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)
Color04_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)
Color05_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)
Color06_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)
Color07_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)
Color08_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)
Color09_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)
Color10_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)

# Create grayscale and color trackbar(s).
cv2.createTrackbar('gs_break_01', 'Grayscale Trackbars', 50, 255, lambda x: None)
cv2.createTrackbar('gs_break_02', 'Grayscale Trackbars', 85, 255, lambda x: None)
cv2.createTrackbar('gs_break_03', 'Grayscale Trackbars', 127, 255, lambda x: None)
cv2.createTrackbar('gs_break_04', 'Grayscale Trackbars', 170, 255, lambda x: None)  
cv2.createTrackbar('gs_break_05', 'Grayscale Trackbars', 210, 255, lambda x: None)
cv2.createTrackbar('gs_break_06', 'Grayscale Trackbars', 230, 255, lambda x: None)
cv2.createTrackbar('gs_break_07', 'Grayscale Trackbars', 240, 255, lambda x: None)
cv2.createTrackbar('gs_break_08', 'Grayscale Trackbars', 245, 255, lambda x: None)
cv2.createTrackbar('gs_break_09', 'Grayscale Trackbars', 250, 255, lambda x: None)
cv2.createTrackbar('Blue_Color01', 'Color01 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Green_Color01', 'Color01 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Red_Color01', 'Color01 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Blue_Color02', 'Color02 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Green_Color02', 'Color02 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Red_Color02', 'Color02 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Blue_Color03', 'Color03 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Green_Color03', 'Color03 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Red_Color03', 'Color03 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Blue_Color04', 'Color04 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Green_Color04', 'Color04 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Red_Color04', 'Color04 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Blue_Color05', 'Color05 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Green_Color05', 'Color05 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Red_Color05', 'Color05 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Blue_Color06', 'Color06 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Green_Color06', 'Color06 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Red_Color06', 'Color06 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Blue_Color07', 'Color07 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Green_Color07', 'Color07 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Red_Color07', 'Color07 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Blue_Color08', 'Color08 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Green_Color08', 'Color08 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Red_Color08', 'Color08 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Blue_Color09', 'Color09 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Green_Color09', 'Color09 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Red_Color09', 'Color09 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Blue_Color10', 'Color10 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Green_Color10', 'Color10 Trackbars', 0, 255, lambda x: None)
cv2.createTrackbar('Red_Color10', 'Color10 Trackbars', 0, 255, lambda x: None)

# Initialize while look control variable. Then start the loop.
keypressed = 1
while (keypressed != 27 and keypressed !=ord('s')):

    # Define the colors of the papers.
    Blue_Color01 = cv2.getTrackbarPos('Blue_Color01', 'Color01 Trackbars')
    Green_Color01 = cv2.getTrackbarPos('Green_Color01', 'Color01 Trackbars')
    Red_Color01 = cv2.getTrackbarPos('Red_Color01', 'Color01 Trackbars')
    Blue_Color02 = cv2.getTrackbarPos('Blue_Color02', 'Color02 Trackbars')
    Green_Color02 = cv2.getTrackbarPos('Green_Color02', 'Color02 Trackbars')
    Red_Color02 = cv2.getTrackbarPos('Red_Color02', 'Color02 Trackbars')
    Blue_Color03 = cv2.getTrackbarPos('Blue_Color03', 'Color03 Trackbars')
    Green_Color03 = cv2.getTrackbarPos('Green_Color03', 'Color03 Trackbars')
    Red_Color03 = cv2.getTrackbarPos('Red_Color03', 'Color03 Trackbars')
    Blue_Color04 = cv2.getTrackbarPos('Blue_Color04', 'Color04 Trackbars')
    Green_Color04 = cv2.getTrackbarPos('Green_Color04', 'Color04 Trackbars')
    Red_Color04 = cv2.getTrackbarPos('Red_Color04', 'Color04 Trackbars')    
    Blue_Color05 = cv2.getTrackbarPos('Blue_Color05', 'Color05 Trackbars')
    Green_Color05 = cv2.getTrackbarPos('Green_Color05', 'Color05 Trackbars')
    Red_Color05 = cv2.getTrackbarPos('Red_Color05', 'Color05 Trackbars')    
    Blue_Color06 = cv2.getTrackbarPos('Blue_Color06', 'Color06 Trackbars')
    Green_Color06 = cv2.getTrackbarPos('Green_Color06', 'Color06 Trackbars')
    Red_Color06 = cv2.getTrackbarPos('Red_Color06', 'Color06 Trackbars')
    Blue_Color07 = cv2.getTrackbarPos('Blue_Color07', 'Color07 Trackbars')
    Green_Color07 = cv2.getTrackbarPos('Green_Color07', 'Color07 Trackbars')
    Red_Color07= cv2.getTrackbarPos('Red_Color07', 'Color07 Trackbars')
    Blue_Color07 = cv2.getTrackbarPos('Blue_Color07', 'Color07 Trackbars')
    Green_Color08 = cv2.getTrackbarPos('Green_Color08', 'Color08 Trackbars')
    Red_Color08 = cv2.getTrackbarPos('Red_Color08', 'Color08 Trackbars')    
    Blue_Color08 = cv2.getTrackbarPos('Blue_Color08', 'Color08 Trackbars')
    Green_Color09 = cv2.getTrackbarPos('Green_Color09', 'Color09 Trackbars')
    Red_Color09 = cv2.getTrackbarPos('Red_Color09', 'Color09 Trackbars')    
    Blue_Color09 = cv2.getTrackbarPos('Blue_Color09', 'Color09 Trackbars')
    Green_Color10 = cv2.getTrackbarPos('Green_Color10', 'Color10 Trackbars')
    Red_Color10 = cv2.getTrackbarPos('Red_Color10', 'Color10 Trackbars')    
    Blue_Color10 = cv2.getTrackbarPos('Blue_Color10', 'Color10 Trackbars')

    # Output the current color settings to the Shell window
    print(f"Color 01: Blue={Blue_Color01}, Green={Green_Color01}, Red={Red_Color01}")
    print(f"Color 02: Blue={Blue_Color02}, Green={Green_Color02}, Red={Red_Color02}")
    print(f"Color 03: Blue={Blue_Color03}, Green={Green_Color03}, Red={Red_Color03}")
    print(f"Color 04: Blue={Blue_Color04}, Green={Green_Color04}, Red={Red_Color04}")
    print(f"Color 05: Blue={Blue_Color05}, Green={Green_Color05}, Red={Red_Color05}")
    print(f"Color 06: Blue={Blue_Color06}, Green={Green_Color06}, Red={Red_Color06}")
    print(f"Color 07: Blue={Blue_Color07}, Green={Green_Color07}, Red={Red_Color07}")
    print(f"Color 08: Blue={Blue_Color08}, Green={Green_Color08}, Red={Red_Color08}")
    print(f"Color 09: Blue={Blue_Color09}, Green={Green_Color09}, Red={Red_Color09}")
    print(f"Color 10: Blue={Blue_Color10}, Green={Green_Color10}, Red={Red_Color10}")

    # Assign the colors to the colored papers. The \ extends the line of code.
    Color01_paper[0:image_height, 0:image_width, 0:image_channels] = \
        [Blue_Color01, Green_Color01, Red_Color01]
    Color02_paper[0:image_height, 0:image_width, 0:image_channels] = \
        [Blue_Color02, Green_Color02, Red_Color02]
    Color03_paper[0:image_height, 0:image_width, 0:image_channels] = \
        [Blue_Color03, Green_Color03, Red_Color03]
    Color04_paper[0:image_height, 0:image_width, 0:image_channels] = \
        [Blue_Color04, Green_Color04, Red_Color04]
    Color05_paper[0:image_height, 0:image_width, 0:image_channels] = \
        [Blue_Color05, Green_Color05, Red_Color05]
    Color06_paper[0:image_height, 0:image_width, 0:image_channels] = \
        [Blue_Color06, Green_Color06, Red_Color06]
    Color07_paper[0:image_height, 0:image_width, 0:image_channels] = \
        [Blue_Color07, Green_Color07, Red_Color07]
    Color08_paper[0:image_height, 0:image_width, 0:image_channels] = \
        [Blue_Color08, Green_Color08, Red_Color08]
    Color09_paper[0:image_height, 0:image_width, 0:image_channels] = \
        [Blue_Color09, Green_Color09, Red_Color09]
    Color10_paper[0:image_height, 0:image_width, 0:image_channels] = \
        [Blue_Color10, Green_Color10, Red_Color10]
    
    # Define the break point for "light" and "dark". Ensure right data type.
    gs_break_01 = cv2.getTrackbarPos('gs_break_01', 'Grayscale Trackbars')
    gs_break_02 = cv2.getTrackbarPos('gs_break_02', 'Grayscale Trackbars')
    gs_break_03 = cv2.getTrackbarPos('gs_break_03', 'Grayscale Trackbars')
    gs_break_04 = cv2.getTrackbarPos('gs_break_04', 'Grayscale Trackbars')
    gs_break_05 = cv2.getTrackbarPos('gs_break_05', 'Grayscale Trackbars')
    gs_break_06 = cv2.getTrackbarPos('gs_break_06', 'Grayscale Trackbars')
    gs_break_07 = cv2.getTrackbarPos('gs_break_07', 'Grayscale Trackbars')
    gs_break_08 = cv2.getTrackbarPos('gs_break_08', 'Grayscale Trackbars')
    gs_break_09 = cv2.getTrackbarPos('gs_break_09', 'Grayscale Trackbars')
    

if gs_break_01 > gs_break_02:
    cv2.setTrackbarPos('gs_break_01', 'Grayscale Trackbars', gs_break_02 - 1)

if gs_break_02 > gs_break_03:
    cv2.setTrackbarPos('gs_break_02', 'Grayscale Trackbars', gs_break_03 - 1)

if gs_break_03 > gs_break_04:
    cv2.setTrackbarPos('gs_break_03', 'Grayscale Trackbars', gs_break_04 - 1)

if gs_break_04 > gs_break_05:
    cv2.setTrackbarPos('gs_break_04', 'Grayscale Trackbars', gs_break_05 - 1)

if gs_break_05 > gs_break_06:
    cv2.setTrackbarPos('gs_break_05', 'Grayscale Trackbars', gs_break_06 - 1)

if gs_break_06 > gs_break_07:
    cv2.setTrackbarPos('gs_break_06', 'Grayscale Trackbars', gs_break_07 - 1)

if gs_break_07 > gs_break_08:
    cv2.setTrackbarPos('gs_break_07', 'Grayscale Trackbars', gs_break_08 - 1)

if gs_break_08 > gs_break_09:
    cv2.setTrackbarPos('gs_break_08', 'Grayscale Trackbars', gs_break_09 - 1)

# Adjusting max values to ensure the trackbars don't exceed their limits

if gs_break_09 > 254:
    cv2.setTrackbarPos('gs_break_09', 'Grayscale Trackbars', 254)

if gs_break_08 > 253:
    cv2.setTrackbarPos('gs_break_08', 'Grayscale Trackbars', 253)

if gs_break_07 > 252:
    cv2.setTrackbarPos('gs_break_07', 'Grayscale Trackbars', 252)

if gs_break_06 > 251:
    cv2.setTrackbarPos('gs_break_06', 'Grayscale Trackbars', 251)

if gs_break_05 > 250:
    cv2.setTrackbarPos('gs_break_05', 'Grayscale Trackbars', 250)

    min_grayscale_for_Color01 = [0, 0, 0]
    max_grayscale_for_Color01 = [gs_break_01, gs_break_01, gs_break_01]
    min_grayscale_for_Color02 = [gs_break_01+1, gs_break_01+1, gs_break_01+1]
    max_grayscale_for_Color02 = [gs_break_02, gs_break_02, gs_break_02]
    min_grayscale_for_Color03 = [gs_break_02+1, gs_break_02+1, gs_break_02+1]
    max_grayscale_for_Color03 = [gs_break_03, gs_break_03, gs_break_03]
    min_grayscale_for_Color04 = [gs_break_03+1, gs_break_03+1, gs_break_03+1]
    max_grayscale_for_Color04 = [gs_break_04, gs_break_04, gs_break_04]
    min_grayscale_for_Color05 = [gs_break_04+1, gs_break_04+1, gs_break_04+1]
    max_grayscale_for_Color05 = [gs_break_05, gs_break_05, gs_break_05]
    min_grayscale_for_Color06 = [gs_break_05+1, gs_break_05+1, gs_break_05+1]
    max_grayscale_for_Color06 = [gs_break_06, gs_break_06, gs_break_06]
    min_grayscale_for_Color07 = [gs_break_06+1, gs_break_06+1, gs_break_06+1]    
    max_grayscale_for_Color07 = [gs_break_07, gs_break_07, gs_break_07]
    min_grayscale_for_Color08 = [gs_break_07+1, gs_break_07+1, gs_break_07+1]
    max_grayscale_for_Color08 = [gs_break_08, gs_break_08, gs_break_08]
    min_grayscale_for_Color09 = [gs_break_08+1, gs_break_08+1, gs_break_08+1]
    max_grayscale_for_Color09 = [gs_break_09, gs_break_09, gs_break_09]
    min_grayscale_for_Color10 = [gs_break_09+1, gs_break_09+1, gs_break_09+1]
    max_grayscale_for_Color10 = [255, 255, 255]

    min_grayscale_for_Color01 = numpy.array(min_grayscale_for_Color01,
                                            dtype="uint8")
    max_grayscale_for_Color01 = numpy.array(max_grayscale_for_Color01,
                                            dtype="uint8")
    min_grayscale_for_Color02 = numpy.array(min_grayscale_for_Color02,
                                            dtype="uint8")
    max_grayscale_for_Color02 = numpy.array(max_grayscale_for_Color02,
                                            dtype="uint8")
    min_grayscale_for_Color03 = numpy.array(min_grayscale_for_Color03,
                                            dtype="uint8")
    max_grayscale_for_Color03 = numpy.array(max_grayscale_for_Color03,
                                            dtype="uint8")
    min_grayscale_for_Color04 = numpy.array(min_grayscale_for_Color04,
                                            dtype="uint8")
    max_grayscale_for_Color04 = numpy.array(max_grayscale_for_Color04,
                                            dtype="uint8")
    min_grayscale_for_Color05 = numpy.array(min_grayscale_for_Color05,
                                            dtype="uint8")
    max_grayscale_for_Color05 = numpy.array(max_grayscale_for_Color05,
                                            dtype="uint8")
    min_grayscale_for_Color06 = numpy.array(min_grayscale_for_Color06,
                                            dtype="uint8")
    max_grayscale_for_Color06 = numpy.array(max_grayscale_for_Color06,
                                            dtype="uint8")
    min_grayscale_for_Color07 = numpy.array(min_grayscale_for_Color07,
                                            dtype="uint8")
    max_grayscale_for_Color07 = numpy.array(max_grayscale_for_Color07,
                                            dtype="uint8")
    min_grayscale_for_Color08 = numpy.array(min_grayscale_for_Color08,
                                            dtype="uint8")
    max_grayscale_for_Color08 = numpy.array(max_grayscale_for_Color08,
                                            dtype="uint8")
    min_grayscale_for_Color09 = numpy.array(min_grayscale_for_Color09,
                                            dtype="uint8")
    max_grayscale_for_Color09 = numpy.array(max_grayscale_for_Color09,
                                            dtype="uint8")
    min_grayscale_for_Color10 = numpy.array(min_grayscale_for_Color10,
                                            dtype="uint8")
    max_grayscale_for_Color10 = numpy.array(max_grayscale_for_Color10,
                                            dtype="uint8")  
    # Create masks.
    block_all_but_the_Color01_parts = cv2.inRange(grayscale_image,
                                                   min_grayscale_for_Color01,
                                                   max_grayscale_for_Color01)
    block_all_but_the_Color02_parts = cv2.inRange(grayscale_image,
                                                   min_grayscale_for_Color02,
                                                   max_grayscale_for_Color02)
    block_all_but_the_Color03_parts = cv2.inRange(grayscale_image,
                                                   min_grayscale_for_Color03,
                                                   max_grayscale_for_Color03)
    block_all_but_the_Color04_parts = cv2.inRange(grayscale_image,
                                                   min_grayscale_for_Color04,
                                                   max_grayscale_for_Color04)
    block_all_but_the_Color05_parts = cv2.inRange(grayscale_image,
                                                   min_grayscale_for_Color05,
                                                   max_grayscale_for_Color05)
    block_all_but_the_Color06_parts = cv2.inRange(grayscale_image,
                                                   min_grayscale_for_Color06,
                                                   max_grayscale_for_Color06)
    block_all_but_the_Color07_parts = cv2.inRange(grayscale_image,
                                                   min_grayscale_for_Color07,
                                                   max_grayscale_for_Color07)
    block_all_but_the_Color08_parts = cv2.inRange(grayscale_image,
                                                   min_grayscale_for_Color08,
                                                   max_grayscale_for_Color08)
    block_all_but_the_Color09_parts = cv2.inRange(grayscale_image,
                                                   min_grayscale_for_Color09,
                                                   max_grayscale_for_Color09)
    block_all_but_the_Color10_parts = cv2.inRange(grayscale_image,
                                                   min_grayscale_for_Color10,
                                                   max_grayscale_for_Color10)

    # Apply masks to create colored parts.
    Color01_parts_of_image = cv2.bitwise_or(Color01_paper, Color01_paper, mask=
                                             block_all_but_the_Color01_parts)
    Color02_parts_of_image = cv2.bitwise_or(Color02_paper, Color02_paper, mask=
                                             block_all_but_the_Color02_parts)
    Color03_parts_of_image = cv2.bitwise_or(Color03_paper, Color03_paper, mask=
                                             block_all_but_the_Color03_parts)
    Color04_parts_of_image = cv2.bitwise_or(Color04_paper, Color04_paper, mask=
                                             block_all_but_the_Color04_parts)
    Color05_parts_of_image = cv2.bitwise_or(Color05_paper, Color05_paper, mask=
                                             block_all_but_the_Color05_parts)
    Color06_parts_of_image = cv2.bitwise_or(Color06_paper, Color06_paper, mask=
                                             block_all_but_the_Color06_parts)
    Color07_parts_of_image = cv2.bitwise_or(Color07_paper, Color04_paper, mask=
                                             block_all_but_the_Color07_parts)
    Color08_parts_of_image = cv2.bitwise_or(Color08_paper, Color08_paper, mask=
                                             block_all_but_the_Color08_parts)
    Color09_parts_of_image = cv2.bitwise_or(Color09_paper, Color09_paper, mask=
                                             block_all_but_the_Color09_parts)
    Color10_parts_of_image = cv2.bitwise_or(Color10_paper, Color10_paper, mask=
                                             block_all_but_the_Color10_parts)
    
    # Combine colored parts to create customized image
    customized_image = cv2.add(Color01_parts_of_image,
                               Color02_parts_of_image)
    customized_image = cv2.add(customized_image, Color03_parts_of_image)
    customized_image = cv2.add(customized_image, Color04_parts_of_image)
    customized_image = cv2.add(customized_image, Color05_parts_of_image)
    customized_image = cv2.add(customized_image, Color06_parts_of_image)
    customized_image = cv2.add(customized_image, Color07_parts_of_image)
    customized_image = cv2.add(customized_image, Color08_parts_of_image)
    customized_image = cv2.add(customized_image, Color09_parts_of_image)
    customized_image = cv2.add(customized_image, Color10_parts_of_image)

    # Display original, grayscale, colored parts, and customized image.
    cv2.imshow('Color01 Parts of Image', Color01_parts_of_image)
    cv2.imshow('Color02 Parts of Image', Color02_parts_of_image)
    cv2.imshow('Color03 Parts of Image', Color03_parts_of_image)
    cv2.imshow('Color04 Parts of Image', Color04_parts_of_image)
    cv2.imshow('Color05 Parts of Image', Color05_parts_of_image)
    cv2.imshow('Color06 Parts of Image', Color06_parts_of_image)
    cv2.imshow('Color07 Parts of Image', Color07_parts_of_image)
    cv2.imshow('Color08 Parts of Image', Color08_parts_of_image)
    cv2.imshow('Color09 Parts of Image', Color09_parts_of_image)
    cv2.imshow('Color10 Parts of Image', Color10_parts_of_image)
    cv2.imshow('Customized Image',customized_image)

    # Give a delay to tell the computer to refresh the page.
    keypressed = cv2.waitKey(1)

# We are outside the loop now, so either "s" or "esc" was pressed.
# Save images if "s" was pressed. Destroy all windows.
if keypressed == ord('s'):
    cv2.imwrite('photo_grayscale_1.jpg',grayscale_image)
    cv2.imwrite('photo_customized_1.jpg',customized_image)
    cv2.destroyAllWindows()
# WaitKey added for Macs to properly end program.
cv2.waitKey(1)