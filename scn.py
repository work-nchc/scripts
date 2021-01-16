from numpy import zeros, arange
from random import shuffle
from pyglet.image import ImageData

width = 1280
height = 720
frame = 300
color_type = 'uint8'
color_max = 255
area = width * height
board = zeros(area, color_type)
idx = arange(area)
shuffle(idx)

for i in range(frame):
    board[idx[i::frame]] = color_max
    image = ImageData(width, height, 'I', board.tobytes())
    image.save('{}.png'.format(i))

# C:\AviUtlPack\3rdparty\ffmpeg.exe -framerate 60 -i %d.png -c:v libx264 -preset ultrafast -qp 0 scn.mp4
