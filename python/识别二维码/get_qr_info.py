from pyzbar.pyzbar import decode
from PIL import Image


def read_qr_code(image_path):
    image = Image.open(image_path)
    qrcodes = decode(image)

    for qr in qrcodes:
        data = qr.data.decode('utf-8')
        print("二维码的内容为: ", data)


if __name__ == '__main__':
    image_path = 'qr_code.png'
    read_qr_code(image_path)
