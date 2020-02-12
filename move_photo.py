from os import walk, mkdir
from time import strftime, sleep
from shutil import move
from PIL import Image

fldr = 'D:/SolidMemory_Face_Rig/Shot_00/'
fldr2 = 'C:/Users/admin/Pictures/digiCamControl/Session1/'
dst = 'Z:/{}/'
name = '{}.jpg'
tag_sn = 42033
sec_sleep = 5
num_old = 0
while True:
    try:
        imgs = next(walk(fldr))[2]
    except StopIteration:
        imgs = []
    if imgs and len(imgs) == num_old:
        sleep(sec_sleep)
        dst_now = dst.format(strftime('%Y_%m_%d_%H_%M_%S'))
        try:
            mkdir(dst_now)
        except FileExistsError:
            pass
        {move(fldr + i,
              dst_now + name.format(Image.open(fldr + i).getexif()[tag_sn]))
         for i in imgs}
        try:
            imgs2 = next(walk(fldr2))[2]
        except StopIteration:
            imgs2 = []
        {move(fldr2 + i,
              dst_now + name.format(Image.open(fldr2 + i).getexif()[tag_sn]))
         for i in imgs2}
    num_old = len(imgs)
    sleep(sec_sleep)
