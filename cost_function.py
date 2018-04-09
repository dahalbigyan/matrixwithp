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
