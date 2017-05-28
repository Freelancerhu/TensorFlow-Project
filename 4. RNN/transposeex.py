import numpy as np

chunk_size = 1
n_chunks = 2 

#quick example data
x = np.ones((1,2,3))
print(x)
print('---')
x = np.transpose(x,(1,0,2))
print(x)
print('---')

x = np.reshape(x, (-1, chunk_size))
print(x)
print('---')

x = np.split(x, n_chunks, 0)
print(x)
print('---')