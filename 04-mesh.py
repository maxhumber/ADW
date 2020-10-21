# https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

import gif

h = .02  # step size in the mesh

X, y = make_moons(noise=0.3, random_state=0)
X = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.4, random_state=42)

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

xx, yy = np.meshgrid(
    np.arange(x_min, x_max, h),
    np.arange(y_min, y_max, h)
)

model = KNeighborsClassifier(3)
model = SVC(gamma=2, C=1, probability=True)

model.fit(X_train, y_train)
score = model.score(X_test, y_test)
Z = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z = Z.reshape(xx.shape)

cm = plt.cm.viridis
first, last = cm.colors[0], cm.colors[-1]
cm_bright = ListedColormap([first, last])
fig, ax = plt.subplots()
ax.contourf(xx, yy, Z, cmap=cm, alpha=.8)
ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright,
           edgecolors='k')
ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright,
           edgecolors='k', alpha=0.6)
ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())
ax.set_xticks(())
ax.set_yticks(())
ax.text(xx.max() - .3, yy.min() + .3, ('%.2f' % score).lstrip('0'),
        size=15, horizontalalignment='right');

# 2

@gif.frame
def plot(gamma, C):
    model = SVC(gamma=gamma, C=C, probability=True)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    Z = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
    Z = Z.reshape(xx.shape)
    cm = plt.cm.viridis
    first, last = cm.colors[0], cm.colors[-1]
    cm_bright = ListedColormap([first, last])
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.contourf(xx, yy, Z, cmap=cm, alpha=.8)
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright,
               edgecolors='k')
    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright,
               edgecolors='k', alpha=0.6)
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xticks(())
    ax.set_yticks(())
    ax.text(xx.max() - .3, yy.min() + .3, ('%.2f' % score).lstrip('0'),
            size=15, horizontalalignment='right')
    fig.suptitle(f"SVC({gamma=}, {C=})")

from itertools import product

gammas = [1/100, 1/10, 1, 10, 100]
Cs = [1/100, 1/10, 1, 10, 100]

gif.options.matplotlib['dpi'] = 200

plot(1, 1)

frames = []
for gamma, C in product(gammas, Cs):
    frame = plot(gamma, C)
    frames.append(frame)

gif.save(frames, "output/mesh.gif", duration=2, unit='s')

# knn

@gif.frame
def plot(model):
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    Z = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
    Z = Z.reshape(xx.shape)
    cm = plt.cm.viridis
    cm_bright = ListedColormap([cm.colors[0], cm.colors[-1]])
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.contourf(xx, yy, Z, cmap=cm, alpha=.8)
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright,
               edgecolors='k')
    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright,
               edgecolors='k', alpha=0.6)
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xticks(())
    ax.set_yticks(())
    ax.text(xx.max() - .3, yy.min() + .3, ('%.2f' % score).lstrip('0'),
            size=15, horizontalalignment='right')
    fig.suptitle(f"KNeighborsClassifier({model.n_neighbors})")

gif.options.matplotlib['dpi'] = 200

frames = []
for n in range(1, 20):
    frame = plot(KNeighborsClassifier(n))
    frames.append(frame)

gif.save(frames, "output/mesh.gif", duration=1, unit='s')
