from sklearn.neighbors import KNeighborsRegressor
from time import time

while True:
    x_low = []
    c_low = []
    d_low = []
    x_high = []
    i_high = []
    file_in = input('input: ')
    file_out = input('output: ')

    with open(file_in) as cloud_in:
        
        head = next(cloud_in), next(cloud_in)

        t = time()
        for data in cloud_in:
            
            point = data.split()
            
            coordinate = tuple(map(float, point[:3]))
            colour = tuple(map(int, point[3:6]))
            intensity = point[6]
            
            if colour[2] < 128:
                x_low.append(coordinate)
                c_low.append(colour)
                d_low.append(data)
            else:
                x_high.append(coordinate)
                i_high.append(intensity)
        print(time() - t)

    t = time()
    regressor = KNeighborsRegressor(1, n_jobs=-1)
    regressor.fit(x_low, c_low)
    c_high = regressor.predict(x_high)
    print(time() - t)

    with open(file_out, 'w') as cloud_out:
        cloud_out.writelines(head)
        t = time()
        for data in d_low:
            cloud_out.write(data)
        for x, c, i in zip(x_high, c_high, i_high):
            cloud_out.write(' '.join(map(str, x)))
            cloud_out.write(' ')
            cloud_out.write(str(min(int(c[0] + float(i) / 3), 255)))
            cloud_out.write(' ')
            cloud_out.write(str(min(int(c[1] + float(i) * 2 / 3), 255)))
            cloud_out.write(' ')
            cloud_out.write(str(max(int(c[2] - float(i)), 0)))
            cloud_out.write(' ')
            cloud_out.write(i)
            cloud_out.write('\n')
        print(time() - t)
