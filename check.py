imgs_all = {
    '303071020882.jpg': '05-2',
    '303071020883.jpg': '13-4',
    '303071020885.jpg': '04-3',
    '303071020886.jpg': '07-2',
    '308071022022.jpg': '15-5',
    '308071022075.jpg': '13-5',
    '308071022076.jpg': '05-5',
    '308071022077.jpg': '01-5',
    '308071022078.jpg': '09-5',
    '308071022079.jpg': '03-5',
    '308071022086.jpg': '07-5',
    '323071012278.jpg': '06-2',
    '323071012280.jpg': '07-3',
    '323071012935.jpg': '13-1',
    '323071012936.jpg': '01-3',
    '323071012993.jpg': '15-1',
    '323071012994.jpg': '10-2',
    '323071014259.jpg': '09-4',
    '323071014274.jpg': '11-4',
    '323071014295.jpg': '03-2',
    '323071014314.jpg': '08-2s',
    '323071014318.jpg': '09-2',
    '323071014325.jpg': '03-4',
    '323071014331.jpg': '01-4',
    '323071014335.jpg': '03-3',
    '323071014338.jpg': '11-1',
    '323071014340.jpg': '10-3',
    '323071014350.jpg': '02-3',
    '318071014357.jpg': '12-3',
    '318071014358.jpg': '11-5',
    '323071014359.jpg': '06-3',
    '323071014360.jpg': '15-4',
    '323071014361.jpg': '01-1',
    '323071014362.jpg': '09-1',
    '323071014364.jpg': '13-3',
    '323071014398.jpg': '15-2',
    '323071014550.jpg': '05-1',
    '323071014567.jpg': '07-1',
    '323071014568.jpg': '14-3',
    '323071014588.jpg': '11-3',
    '323071014592.jpg': '05-4',
    '323071014595.jpg': '07-4',
    '303071016106.jpg': '11-2',
    '313071008283.jpg': '08-3',
    '313071008285.jpg': '13-2',
    '313071008286.jpg': '09-3',
    '313071008295.jpg': '15-3',
    '313071008296.jpg': '05-3',
    '313071008297.jpg': '03-1',
    '313071008299.jpg': '01-2',
}

from os import walk
fldr = input('folder: ')

try:
    imgs = set(map(str.lower, next(walk(fldr))[2]))
except StopIteration:
    imgs = set()

{print(i, imgs_all[i]) for i in imgs_all if i.lower() not in imgs}
