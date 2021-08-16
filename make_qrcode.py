# make QR Code for website

import qrcode as qr
from qrcode.constants import ERROR_CORRECT_H


def make_qrcode(website_url):
    qrc = qr.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_H,
        box_size=10, border=4,
    )
    qrc.add_data(website_url)
    qrc.make(fit=True)
    img = qrc.make_image(fill_color="black", back_color="white")

    return img.save('img/qrcode.png')


website_url = input('Enter your website link: ')


make_qrcode(website_url)
