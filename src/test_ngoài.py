import numpy as np
def get_data(path):
    data = np.load(path, allow_pickle= True)
    return data
print(get_data('./data/digits.npy'))