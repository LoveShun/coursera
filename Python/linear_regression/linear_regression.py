# -*- coding: utf-8 -*-
# 线性回归的Python实现

import numpy as np


class LinearRegression(object):
    def __init__(self, X, y, init_theta, alpha, max_iter=1000):
        self.X = np.column_stack([np.ones(len(X)), X])
        self.y = y
        self.theta = init_theta
        self.alpha = alpha
        self.m = len(y)
        self.n = len(self.X[0])
        self.max_iter = max_iter
        self.train()

    def cal_h(self):
        return np.dot(self.X, self.theta)

    def cal_loss(self):
        diff = self.cal_h() - self.y
        return np.sum(np.dot(diff.T, diff)) / (2 * self.m)

    def gradient_descend(self):
        diff = self.cal_h() - self.y
        gradient = self.alpha * np.dot(self.X.T, diff) / (2 * self.m)
        self.theta -= gradient

    def train(self):
        for i in range(self.max_iter):
            self.gradient_descend()

    def predict(self, X):
        X = np.column_stack([np.ones(len(X)), X])
        return np.dot(X, self.theta)

#
if __name__ == '__main__':
    X = np.array([[1, 1, 1],
                  [2, 2, 2]])
    y = np.array([[1],
                  [2]])
    init_theta = np.ones(len(X[0])+1).reshape(-1, 1)
    alpha = 0.1
    linear_regression = LinearRegression(X, y, init_theta, alpha)
    test_X = np.array([[5, 5, 5],
                       [6, 6, 6]])
    print(linear_regression.predict(test_X))
