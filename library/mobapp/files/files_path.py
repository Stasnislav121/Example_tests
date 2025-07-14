import os

DIR_PATH = os.path.abspath(os.path.dirname(__file__))

PACKAGE_IMAGE = {
    'IMAGE_JPG': os.path.join(DIR_PATH, 'package_jpg.jpg'),
    'IMAGE_BMP': os.path.join(DIR_PATH, 'package_bmp.bmp'),
    'IMAGE_WEBP': os.path.join(DIR_PATH, 'package_webp.webp'),
    'IMAGE_PNG': os.path.join(DIR_PATH, 'package_png.png'),
    'IMAGE_HEIF': os.path.join(DIR_PATH, 'package_heif.heif')
}
