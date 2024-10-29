import qrcode   #pip install qrcode
from PIL import Image  #pip install "qrcode[pil]"

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)


qr.add_data("https://www.facebook.com/")
qr.make(fit=True)
#generate image with colors
img=qr.make_image(fill_color="red",back_color="yellow")
img.save("facebook.png")