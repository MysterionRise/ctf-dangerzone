from PIL import Image, ImageEnhance, ImageFilter
import pyzbar.pyzbar as pyzbar
import cv2
import numpy as np


def convert_to_greyscale(img):
    greyscale_img = img.convert('L')
    return greyscale_img


def create_negative(img):
    negative_img = Image.eval(img, lambda x: 255 - x)
    return negative_img


img = Image.open('qr_mosaic.bmp')
img_width, img_height = img.size
num_rows = 25
num_columns = 40
qr_width = img_width // num_columns
qr_height = img_height // num_rows

decoded_data = []
counter = 0

for row in range(num_rows):
    for col in range(num_columns):

        left = int(col * qr_width)
        upper = int(row * qr_height)
        right = int(left + qr_width)
        lower = int(upper + qr_height)
        bbox = (left, upper, right, lower)
        qr_img = img.crop(bbox)

        decoded_objects = pyzbar.decode(qr_img)
        if decoded_objects:
            data = decoded_objects[0].data.decode('utf-8')
            decoded_data.append(data)
        else:
            qr_img2 = convert_to_greyscale(qr_img)
            qr_img2 = create_negative(qr_img)
            decoded_objects_v2 = pyzbar.decode(qr_img2)
            if decoded_objects_v2:
                data = decoded_objects_v2[0].data.decode('utf-8')
                decoded_data.append(data)
            else:
                qr_img3 = create_negative(qr_img)
                enhancer = ImageEnhance.Contrast(qr_img3)
                qr_img3 = enhancer.enhance(3.0)
                decoded_objects_v3 = pyzbar.decode(qr_img3)
                if decoded_objects_v3:
                    data = decoded_objects_v3[0].data.decode('utf-8')
                    decoded_data.append(data)
                else:
                    detector = cv2.QRCodeDetector()
                    data, vertices_array, binary_qrcode = detector.detectAndDecode(
                        np.array(qr_img))
                    if vertices_array is not None:
                        decoded_data.append(data)
                    else:
                        is_found = False
                        thresh = 0
                        while not is_found and thresh <= 255:
                            fn = lambda x: 255 if x > thresh else 0
                            qr_img4 = qr_img.convert('L').point(fn, mode='1')
                            decoded_objects_v4 = pyzbar.decode(qr_img4)
                            if decoded_objects_v4:
                                data = decoded_objects_v4[0].data.decode(
                                    'utf-8')
                                decoded_data.append(data)
                                is_found = True
                            thresh += 1
                        if not is_found:
                            counter += 1
                            print(f" {row}, {col} ")
        decoded_data.append(f" {row}, {col} \n")

result = ''.join(decoded_data)

print("Decoded Data:")
print(result)
print(counter)
