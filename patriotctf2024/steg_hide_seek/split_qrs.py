from PIL import Image
import os

# Load the image
img = Image.open('qr_mosaic.bmp')

# Get image dimensions
img_width, img_height = img.size

# Grid dimensions (adjust if necessary)
num_rows = 25  # Number of rows in the grid
num_columns = 40  # Number of columns in the grid

# Calculate the size of each QR code
qr_width = img_width / num_columns
qr_height = img_height / num_rows

# Create an output directory for the individual QR codes
output_dir = 'qr_codes_split'
os.makedirs(output_dir, exist_ok=True)

# Loop over the grid and save each QR code
for row in range(num_rows):
    for col in range(num_columns):
        # Calculate bounding box for each QR code
        left = int(col * qr_width)
        upper = int(row * qr_height)
        right = int((col + 1) * qr_width)
        lower = int((row + 1) * qr_height)
        bbox = (left, upper, right, lower)

        # Crop the QR code from the image
        qr_img = img.crop(bbox)

        # Save the cropped QR code image
        output_filename = f'{output_dir}/{row}_{col}.bmp'
        qr_img.save(output_filename)

print("All QR codes have been saved to the 'qr_codes_split' directory.")
