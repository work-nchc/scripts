from os import walk
from shutil import move
from PIL import Image

fldr = 'C:/Users/admin/Pictures/digiCamControl/Session1/'
dst = (
    'D:/SolidMemory_Face_Rig/Shot_00/'
    'Solidmemory_NCHC_RIG__Canon EOS 800D ({}).JPG'
)
tag_sn = 42033

try:
    imgs = sorted(next(walk(fldr))[2])
except StopIteration:
    imgs = []

{move(fldr + i, dst.format(Image.open(fldr + i).getexif()[tag_sn]))
 for i in imgs}
