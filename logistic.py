import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
path = os.getcwd() + '/data2.txt'
data = pd.read_csv(path, header=None, names=['Exam1', 'Exam2', 'Admitted'])

from cost_function import sigmoid

theta = np.zeros(3)
data.insert(0, 'Ones', 1)
cols = data.shape[1]
x = data.iloc[:,0:cols-1]
y = data.iloc[:, cols-1:cols]
x = np.array(x.values)
y = np.array(y.values)
theta = np.matrix(theta)
x = np.matrix(x)
parameters = int(theta.ravel().shape[1])
grad = np.zeros(parameters)
print(grad)
