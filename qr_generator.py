import qrcode
import os

def generate_qr(url):
    # ensure static folder exists
    os.makedirs("static", exist_ok=True)

    path = os.path.join("static", "qr.png")

    img = qrcode.make(url)
    img.save(path)

    return path