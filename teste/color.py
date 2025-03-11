import qrcode.constants


qr = qrcode.QRCode(
    #entre 1 et 40
    version=3,
    box_size=3,
    border=5

)

qr.add_data('https://github.com/yanis26x')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="blue")
img.save('qrcode26x.png')