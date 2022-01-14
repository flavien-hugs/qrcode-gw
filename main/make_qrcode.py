# make QR Code for website

import qrcode as qr
from qrcode.constants import ERROR_CORRECT_H
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer


def make_qrcode(website_url):
    qrc = qr.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_H,
        box_size=10, border=4,
    )
    qrc.add_data(website_url)
    qrc.make(fit=True)
    img = qrc.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        embeded_image_path="favicon.png"
    )
    return img.save('img/qrcode.png')
