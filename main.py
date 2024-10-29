import qrcode as qr   #pip install qrcode
img = qr.make("https://www.youtube.com/")
img.save("youtube.png")