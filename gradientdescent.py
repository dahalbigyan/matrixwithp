#Linear Hypothesis Function
'''
h(x) = m0 + m1x
'''
# Task: Parameters of our model are: m0 and m1. Adjust these values to minimize cost function
# Training Data Part
# xi => yi

# batch gradient algorithm
# each iteration performs the update
"""
cost_function(j(m)) = 1/m(∑ from i to m)((hm)(x^i) - y^i)^2
"""

from numpy import loadtxt, zeros, ones, array, linspace, logspace
from pylab import scatter, show, title, xlabel, ylabel, plot, contour
from cost_function import compute_cost

# load the data set
data = loadtxt('data1.txt', delimiter=',')
#plot the data
# scatter(data[:, 0], data[:, 1], marker='o', c='b')
# title('Profits distribution')
# xlabel('Population of City in 10,000s')
# ylabel('Profit in $10,000s')
# show()


x = data[:, 0]
y = data[:, 1]
# number of training size
m = y.size
# add a column of ones to X(interception data)
it = ones(shape=(m,2))
it[:,1] = x

# Initialize theta parameters
theta = zeros(shape=(2,1))
cost = compute_cost(it,y,theta)
print(it[:,1])
print(it[:,0])
