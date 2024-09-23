import os
import cv2
import numpy as np
from PIL import Image
import pyzbar.pyzbar as pyzbar
import colorsys

# Input directory containing individual QR code images
input_dir = 'qr_codes_split'

# List to hold data for each QR code: (brightness, decoded_data, row, col)
qr_data_list = []

def calculate_metric(img_pil, metric):
    img_np = np.array(img_pil)
    if metric == 'luminosity':
        # Convert to grayscale using luminosity formula
        R, G, B = img_np[:,:,0], img_np[:,:,1], img_np[:,:,2]
        luminosity = 0.21 * R + 0.72 * G + 0.07 * B
        return np.mean(luminosity)
    elif metric == 'lightness':
        # Lightness from HSL
        R, G, B = img_np[:,:,0], img_np[:,:,1], img_np[:,:,2]
        max_rgb = np.maximum.reduce([R, G, B])
        min_rgb = np.minimum.reduce([R, G, B])
        lightness = (max_rgb + min_rgb) / 2
        return np.mean(lightness)
    elif metric == 'value':
        # Value from HSV
        R, G, B = img_np[:,:,0], img_np[:,:,1], img_np[:,:,2]
        value = np.maximum.reduce([R, G, B])
        return np.mean(value)
    elif metric == 'saturation':
        # Saturation from HSV
        R, G, B = img_np[:,:,0], img_np[:,:,1], img_np[:,:,2]
        max_rgb = np.maximum.reduce([R, G, B])
        min_rgb = np.minimum.reduce([R, G, B])
        delta = max_rgb - min_rgb
        saturation = np.divide(delta, max_rgb, out=np.zeros_like(delta), where=max_rgb!=0)
        return np.mean(saturation) * 255
    elif metric == 'hue':
        # Hue from HSV
        img_hsv = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2HSV)
        hue = img_hsv[:,:,0]
        return np.mean(hue)
    elif metric == 'contrast':
        # Contrast as the difference between max and min pixel intensities
        gray = img_pil.convert('L')
        gray_np = np.array(gray)
        contrast = gray_np.max() - gray_np.min()
        return contrast
    elif metric == 'std_dev':
        # Standard deviation of pixel intensities
        gray = img_pil.convert('L')
        gray_np = np.array(gray)
        return np.std(gray_np)
    else:
        raise ValueError(f"Unknown metric: {metric}")
# Function to sort filenames based on row and column numbers
def sort_filenames(filenames):
    sorted_files = sorted(filenames, key=lambda x: (
        int(x.split('_')[0]), int(x.split('_')[1].split('.')[0])
    ))
    return sorted_files

# Get all filenames in the input directory
filenames = [f for f in os.listdir(input_dir) if f.endswith('.bmp')]
filenames = sort_filenames(filenames)

# Process each QR code image
for filename in filenames:
    filepath = os.path.join(input_dir, filename)
    # Extract row and column from filename
    row_col = filename.replace('.bmp', '').split('_')
    row = int(row_col[0])
    col = int(row_col[1])

    # Open image using PIL
    img_pil = Image.open(filepath)

    img_np = np.array(img_pil)
    # Calculate the average RGB color
    avg_color_per_row = np.average(img_np, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    avg_rgb = tuple(avg_color.astype(int))

    # Convert RGB to HSV to get the hue
    # Normalize RGB values to [0, 1]
    r_norm = avg_rgb[0] / 255.0
    g_norm = avg_rgb[1] / 255.0
    b_norm = avg_rgb[2] / 255.0

    # Convert to HSV
    h, s, v = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)
    hue_degrees = h * 360  # Convert hue to degrees for better interpretation

    # Use hue as the metric value for sorting
    metric_value = hue_degrees



    # Append the data to the list
    qr_data_list.append({
        'metric_value': metric_value,
        'row': row,
        'col': col
    })

# Sort the QR codes by brightness from darkest to lightest
qr_data_list.sort(key=lambda x: -x['metric_value'])

# Concatenate the decoded data in the new order
# sorted_decoded_data = ''.join([item['data'] for item in qr_data_list])

print("Concatenated Decoded Data (from darkest to lightest):")
print(qr_data_list)
