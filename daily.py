from numpy import zeros
from glob import glob

y0 = 2020
y1 = 2021
table = zeros((384 * (y1 - y0 + 1), 8))
head = 'date\t0 dl\t0 vdi\t1 dl\t1 vdi\t2 dl\t2 vdi\t3 dl\t3 vdi'

r_d = lambda d: 32 * (12 * (int(d[0]) - y0) + int(d[1]) - 1) + int(d[2])
d_r = lambda r: (r // 384 + y0, r % 384 // 32 + 1, r % 32)

accounts = {}
with open('accounts.csv') as file:
    for data in file:
        data = data.split()
        accounts[data[0]] = int(data[1])

for filename in glob('users_vdi/*'):
    name = filename.split('_')[-1].split('.')[0]
    if name not in accounts:
        print(name)
        break
    with open(filename) as file:
        next(file)
        for data in file:
            data = data.split('\t')
            if 'SU_total' == data[0]:
                break
            if data[1]:
                day = data[1].split('T')[0].split('-')
                if y0 <= int(day[0]) <= y1:
                    table[r_d(day), 2 * accounts[name] + 1] += float(data[-1])

for filename in glob('users_dl/*'):
    name = filename.split('_')[-1].split('.')[0]
    if name not in accounts:
        print(name)
        break
    with open(filename, encoding='utf-8') as file:
        next(file)
        for data in file:
            data = data.split()
            if 'SU_total' == data[0]:
                break
            day = data[0].split('T')[0].split('-')
            if y0 <= int(day[0]) <= y1:
                table[r_d(day), 2 * accounts[name]] += float(data[-1])

with open('total.csv', 'w') as file:
    print(head, file=file)
    for row in range(len(table)):
        day = d_r(row)
        if day[-1]:
            print('{}-{}-{}'.format(*day), end='\t', file=file)
            print(*table[row], sep='\t', file=file)
        else:
            print(file=file)
