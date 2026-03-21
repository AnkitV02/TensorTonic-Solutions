import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    X = np.array(X)
    y = np.array(y).reshape(-1, 1)

    n, d = X.shape

    W = np.zeros((d, 1))
    b = 0.0

    for _ in range(steps):
        z = np.dot(X, W) + b
        y_pred = _sigmoid(z)

        w_update = (1/n) * np.dot(X.T, (y_pred - y))
        b_update = np.mean(y_pred - y)

        W -= lr * w_update
        b -= lr * b_update
    W = W.reshape(-1)
    return W, b