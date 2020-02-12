from glob import glob
from os import mkdir
from time import strftime, sleep
from shutil import move
from PIL import Image

src = (
    'D:/SolidMemory_Face_Rig/Shot_00/*.jpg',
    'C:/Users/admin/Pictures/digiCamControl/Session1/*.jpg',
)
dst = 'Z:/{}/'
name = '{}.jpg'
tag_sn = 42033
sec_sleep = 5

num_old = 0
while True:
    imgs = sum(map(glob, src), [])
    if imgs and len(imgs) == num_old:
        dst_now = dst.format(strftime('%Y_%m_%d_%H_%M_%S'))
        try:
            mkdir(dst_now)
        except FileExistsError:
            pass
        for i in imgs:
            try:
                move(i, dst_now + name.format(Image.open(i).getexif()[tag_sn]))
            except OSError:
                pass
    num_old = len(imgs)
    sleep(sec_sleep)
