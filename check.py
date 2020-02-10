imgs_all = {
    'Solidmemory_NCHC_RIG__Canon EOS 800D (303071020882).JPG': '05-2',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (303071020883).JPG': '13-4',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (303071020885).JPG': '04-3',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (303071020886).JPG': '07-2',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (308071022022).JPG': '15-5',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (308071022075).JPG': '13-5',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (308071022076).JPG': '05-5',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (308071022077).JPG': '01-5',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (308071022078).JPG': '09-5',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (308071022079).JPG': '03-5',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (308071022086).JPG': '07-5',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071012278).JPG': '06-2',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071012280).JPG': '07-3',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071012935).JPG': '13-1',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071012936).JPG': '01-3',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071012993).JPG': '15-1',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071012994).JPG': '10-2',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014259).JPG': '09-4',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014274).JPG': '11-4',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014295).JPG': '03-2',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014314).JPG': '08-2s',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014318).JPG': '09-2',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014325).JPG': '03-4',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014331).JPG': '01-4',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014335).JPG': '03-3',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014338).JPG': '11-1',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014340).JPG': '10-3',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014350).JPG': '02-3',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (318071014357).JPG': '12-3',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (318071014358).JPG': '11-5',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014359).JPG': '06-3',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014360).JPG': '15-4',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014361).JPG': '01-1',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014362).JPG': '09-1',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014364).JPG': '13-3',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014398).JPG': '15-2',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014550).JPG': '05-1',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014567).JPG': '07-1',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014568).JPG': '14-3',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014588).JPG': '11-3',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014592).JPG': '05-4',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (323071014595).JPG': '07-4',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (303071016106).JPG': '11-2',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (313071008283).JPG': '08-3',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (313071008285).JPG': '13-2',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (313071008286).JPG': '09-3',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (313071008295).JPG': '15-3',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (313071008296).JPG': '05-3',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (313071008297).JPG': '03-1',
    'Solidmemory_NCHC_RIG__Canon EOS 800D (313071008299).JPG': '01-2',
}

from os import walk
fldr = input('folder: ')

try:
    imgs = set(map(str.lower, next(walk(fldr))[2]))
except StopIteration:
    imgs = set()

{print(i, imgs_all[i]) for i in imgs_all if i.lower() not in imgs}
