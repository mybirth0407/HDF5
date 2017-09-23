import numpy as np
import h5py

# write
write_arr = np.array([1,2,3,4,5,6,7,8])
h5f = h5py.File('test.h5', 'w')
h5f.create_dataset('arr', data=write_arr)
h5f.close()

# read
h5f = h5py.File('test.h5', 'r')
read_arr = h5f['arr'][:]
h5f.close()

print(b)
