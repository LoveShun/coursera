# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


class LinearRegression(object):
    def __init__(self, train_X, train_y, init_theta, alpha, max_iter=1000):
        self.X = np.column_stack([np.ones(len(train_X)), train_X])
        self.y = train_y
        self.m = len(self.X)
        self.n = len(self.X[0])
        self.theta = init_theta
        self.alpha = alpha
        self.max_iter = max_iter

    @property
    def h(self):
        return np.dot(self.X, self.theta)

    @property
    def loss(self):
        diff = self.h - self.y
        return np.sum(np.dot(diff.T, diff)) / (2 * self.m)

    def gradient_descend(self):
        diff = self.h - self.y
        gradient = self.alpha * np.dot(self.X.T, diff) / (2 * self.m)
        self.theta -= gradient

    def train(self):
        loss = []
        for i in range(self.max_iter):
            self.gradient_descend()
            loss.append(self.loss)
        return loss

    def predict(self, test_X):
        test_X = np.column_stack([np.ones(len(test_X)), test_X])
        return np.dot(test_X, self.theta)



if __name__ == '__main__':
    X = np.array([[1, 2, 3, 4],
                  [2, 3, 4, 5]])
    y = np.array([[4],
                  [6]])
    init_theta = np.ones(len(X[0]) + 1).reshape(-1, 1)
    alpha = 0.01
    linear_regression = LinearRegression(X, y, init_theta, alpha, max_iter=10)
    loss = linear_regression.train()
    plt.plot(loss)
    test_X = np.array([[5, 5, 5, 5],
                       [6, 6, 6, 5]])
    print(linear_regression.predict(test_X))
    plt.show()
