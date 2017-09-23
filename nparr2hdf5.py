import numpy as np
import h5py

# write
a = np.array([1,2,3,4,5,6,7,8])
h5f = h5py.File('test.h5', 'w')
h5f.create_dataset('arr', data=a)
h5f.close()

# read
h5f = h5py.File('test.h5', 'r')
b = h5f['arr'][:]
h5f.close()

print(b)
print(type(b))
print(b.shape)
