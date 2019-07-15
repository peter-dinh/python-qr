import pyqrcode

qr = pyqrcode.create("dinhdinh")
qr.png("dinh.png", scale=6)
