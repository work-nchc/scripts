from numpy import array, zeros
from joblib import Parallel, delayed

__all__ = ['dim_space', 'point_cloud', 'voxel_grid']

dim_space = 3

class point_cloud(object):
    
    def __init__(
        self, data, order=None, field=None, space=None, *args, **kwargs
    ):
        self.dim = data.shape[1]
        if field is None:
            field = list(map(str, range(self.dim)))
        if space is None:
            space = dim_space
        if order is None:
            self.data = array(data)
        else:
            self.data = array(data[data[:, order].argsort()])
        self.field = list(field)
        self.space = space
    
    def __getitem__(self, key):
        attr = dict(self.__dict__)
        attr['data'] = self.data[key]
        return type(self)(**attr)
    
    def simplify(self, leaf, n_jobs=1):
        n_jobs = max(int(n_jobs), 1)
        b = len(self.data) // n_jobs + 1
        vg = voxel_grid(self[:0], leaf)
        for vg_temp in Parallel(n_jobs)(delayed(voxel_grid)(
            self[b*i: b*(i+1)], leaf
        ) for i in range(n_jobs)):
            vg.merge(vg_temp.grid)
        return vg.mean()

class voxel_grid(object):
    
    def __init__(self, cloud, leaf):
        self.leaf = leaf
        self.grid = {}
        self.dim = cloud.data.shape[1] + 1
        for pt in cloud.data:
            vox = tuple(pt[:cloud.space] // leaf)
            if vox not in self.grid:
                self.grid[vox] = zeros(self.dim)
            self.grid[vox][:-1] += pt
            self.grid[vox][-1] += 1.
    
    def merge(self, value):
        for vox in value:
            if vox not in self.grid:
                self.grid[vox] = zeros(self.dim)
            self.grid[vox] += value[vox]
    
    def mean(self):
        cloud_vox = array(tuple(self.grid.values()))
        cloud_vox[:, :-1] /= cloud_vox[:, -1:]
        return cloud_vox[:, :-1]
