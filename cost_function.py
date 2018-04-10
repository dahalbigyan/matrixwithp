import numpy as np

def compute_cost(x,y,theta):
    m = y.size
    predictions = x.dot(theta).flatten()
    sqErrors = (predictions-y)**2
    J = (1.0/(2*m)) * sqErrors.sum()
    return J

def gradient_descent(x,y, theta, alpha, num_iters):
    m = y.size
    J_history = np.zeros(shape=(num_iters, 1))
    for i in range(num_iters):
        predictions = x.dot(theta).flatten()
        errors_x1 = (predictions - y) * x[:, 0]
        errors_x2 = (predictions - y) * x[:, 1]
        theta[0][0] = theta[0][0] - alpha * (1.0 / m) * errors_x1.sum()
        theta[1][0] = theta[1][0] - alpha * (1.0 / m) * errors_x2.sum()

        J_history[i, 0] = compute_cost(X, y, theta)
    return theta, J_history

def sigmoid(z):
    return 1 / (1+np.exp(-z))

def sigmoid_cost(x,y, theta):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    second = np.multiply((1 - y), np.log(1 - sigmoid(X * theta.T)))
    return np.sum(first - second) / (len(X))

def sigmoid_gradient(theta, x, y):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)

    parameters = int(theta.ravel().shape[1])
    grad = np.zeros(parameters)

    error = sigmoid(X * theta.T) - y

    for i in range(parameters):
        term = np.multiply(error, X[:,i])
        grad[i] = np.sum(term) / len(X)

    return grad
