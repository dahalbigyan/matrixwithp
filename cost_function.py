def compute_cost(x,y,theta):
    m = y.size
    predictions = x.dot(theta).flatten()
    sqErrors = (predictions-y)**2
    J = (1.0/(2*m)) * sqErrors.sum()
    return J
