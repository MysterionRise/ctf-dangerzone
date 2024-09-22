import pyshark
import matplotlib.pyplot as plt

# Initialize variables
x = 0
y = 0
positions = [(x, y)]

# Open the pcapng file
capture = pyshark.FileCapture('capture.pcapng',
                              display_filter='usb.capdata')

for packet in capture:
    try:
        # Extract the raw HID data
        hid_raw_data = packet.usb.capdata
        hid_bytes = bytes.fromhex(hid_raw_data)

        # Ensure the HID report is at least 3 bytes
        if len(hid_bytes) < 3:
            continue

        # Extract movement data
        buttons = hid_bytes[0]
        x_move = hid_bytes[1]
        y_move = hid_bytes[2]

        # Convert from unsigned to signed
        x_move = x_move - 256 if x_move > 127 else x_move
        y_move = y_move - 256 if y_move > 127 else y_move

        # Update positions
        x += x_move
        y += y_move
        positions.append((x, y))
    except AttributeError:
        continue

# Plot the movements
x_coords, y_coords = zip(*positions)
plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords)
plt.title('Mouse Movements')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.show()
