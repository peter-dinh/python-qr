# Create and Decode QRCode By Python Code

### Requirement:
``` shell
numpy==1.16.4
opencv-python==4.1.0.25
Pillow==6.0.0
pymaging==0.1
pypng==0.0.19
PyQRCode==1.2.1
python-thumbnails==0.5.1
pyzbar==0.1.8
qrcode==6.1
```
### Install

#### Install zBar
```shell
sudo apt-get install libzbar0
```

#### Install library
```shell
pip install -r req.txt
```

### Usage

#### Create QR image with qrcode
```python
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('dinhdinh')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("dinh.png")
```

#### Create QR image with pyqrcode
```python
import pyqrcode

qr = pyqrcode.create("dinhdinh")
qr.png("dinh.png", scale=6)
```

#### Decode 
```python
from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
 
def decode(im) : 
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(im)
 
  # Print results
  for obj in decodedObjects:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')
     
  return decodedObjects
 
 
# Display barcode and QR code location  
def display(im, decodedObjects):
 
  # Loop over all decoded objects
  for decodedObject in decodedObjects: 
    points = decodedObject.polygon
 
    # If the points do not form a quad, find convex hull
    if len(points) > 4 : 
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else : 
      hull = points;
     
    # Number of points in the convex hull
    n = len(hull)
 
    # Draw the convext hull
    for j in range(0,n):
      cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)
 
  # Display results 
  cv2.imshow("Results", im);
  cv2.waitKey(0);
 
   
# Main 
if __name__ == '__main__':
 
  # Read image
  im = cv2.imread('dinh.png')
 
  decodedObjects = decode(im)
  display(im, decodedObjects)
```

### Related
![Barcode reader with Python, OpenCV and Pyzbar](https://cvisiondemy.com/barcode-reader-with-python-opencv-and-pyzbar/ "Barcode reader with Python, OpenCV and Pyzba")
![Barcode and QR code Scanner using ZBar and OpenCV](https://www.learnopencv.com/barcode-and-qr-code-scanner-using-zbar-and-opencv/ "Barcode and QR code Scanner using ZBar and OpenCV")




