import numpy as np
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot

def local_regression(x0, X, Y, tau):
    # add bias term
    x0 = np.r_[1, x0]  # Add one to avoid the loss in information
    X = np.c_[np.ones(len(X)), X]
    # fit model: normal equations with kernel
    xw = X.T * radial_kernel(x0, X, tau)  # XTranspose * W
    # @ Matrix Multiplication or Dot Product
    beta = np.linalg.pinv(xw @ X) @ xw @ Y
    # predict value
    return x0 @ beta  # @ Matrix Multiplication or Dot Product for prediction

def radial_kernel(x0, X, tau):
    return np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau * tau))


n = 1000
X = np.linspace(-3, 3, num=n)
Y = np.log(np.abs(X ** 2 - 1) + .5)
X += np.random.normal(scale=.1, size=n)
domain = np.linspace(-3, 3, num=300)

def plot_lwr(tau):
    # prediction through regression
    prediction = [local_regression(x0, X, Y, tau) for x0 in domain]
    plot = figure(plot_width=400, plot_height=400)
    plot.scatter(X, Y, alpha=.3)
    plot.line(domain, prediction, line_width=2, color='red')
    return plot

# Plotting the curves with 0.01 tau
show(gridplot([[plot_lwr(0.01)]]))
