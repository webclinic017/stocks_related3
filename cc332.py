import numpy as np
data = np.random.normal(5, 10, size=(10,))

from bayespy.nodes import GaussianARD, Gamma
mu = GaussianARD(0, 1e-6)
tau = Gamma(1e-6, 1e-6)
y = GaussianARD(mu, tau, plates=(10,))

y.observe(data)

from bayespy.inference import VB
Q = VB(mu, tau, y)
Q.update(repeat=20)

import bayespy.plot as bpplt
bpplt.pyplot.subplot(2, 1, 1)

bpplt.pdf(mu, np.linspace(-10, 20, num=100), color='k', name=r'\mu')

bpplt.pyplot.subplot(2, 1, 2)

bpplt.pdf(tau, np.linspace(1e-6, 0.08, num=100), color='k', name=r'\tau')

bpplt.pyplot.tight_layout()
bpplt.pyplot.show()

from bayespy.nodes import Gaussian
X = Gaussian([2, 5], [[1.0, 0.3], [0.3, 1.0]])

from bayespy.nodes import Gaussian, Wishart
mu = Gaussian([0, 0], [[1e-6, 0],[0, 1e-6]])
Lambda = Wishart(2, [[1, 0], [0, 1]])
X = Gaussian(mu, Lambda)
X = Gaussian(mu, Lambda, name='x')
from bayespy.nodes import Dot
Y = Dot(X, X)
from bayespy.nodes import Dot
Z = Gaussian(X, [[1,0], [0,1]])
Y = Dot(X, Z)

# Effects of the nodes on inference

y = Gaussian(mu, Lambda, plates=(10,30))
y_0 = y[0]
y_0.plates

y_even = y[:,::2]
y_even.plates

y_complex = y[:5, 10:20:5]
y_complex.plates

from bayespy.nodes import Gaussian, Wishart
mu = Gaussian([0, 0], [[1e-6, 0],[0, 1e-6]], plates=(10,1))
Lambda = Wishart(2, [[1, 0], [0, 1]], plates=(1,30))
X = Gaussian(mu, Lambda)

import numpy as np
mu = [ [0,0], [1,1], [2,2] ]
Lambda = [ [[1.0, 0.0],
...             [0.0, 1.0]],
...            [[1.0, 0.9],
...             [0.9, 1.0]],
...            [[1.0, -0.3],
...             [-0.3, 1.0]] ]
X = Gaussian(mu, Lambda)
np.shape(mu)
np.shape(Lambda)
X.plates

from bayespy.nodes import Gaussian, Wishart, Categorical, Mixture
mu = Gaussian([[0], [0], [0]], [ [[1]], [[1]], [[1]] ])
Lambda = Wishart(1, [ [[1]], [[1]], [[1]]])
Z = Categorical([1/3, 1/3, 1/3], plates=(100,))
X = Mixture(Z, Gaussian, mu, Lambda)
mu.plates

Lambda.plates

Z.plates

X.plates

from bayespy.nodes import GaussianARD, Gamma
tau = Gamma(1, 1, plates=(5,4,3))
X = GaussianARD(0, tau, shape=(4,3))
tau.plates

X.plates

# Example model: Principal component analy

D = 3
X = GaussianARD(0, 1,shape=(D,),plates=(1,100),name='X')

alpha = Gamma(1e-3, 1e-3,plates=(D,),name='alpha')

C = GaussianARD(0, alpha,shape=(D,),plates=(10,1),name='C')

F = Dot(C, X)

F.plates
tau = Gamma(1e-3, 1e-3, name='tau')
Y = GaussianARD(F, tau, name='Y')


# Observing nodes
c = np.random.randn(10, 2)
x = np.random.randn(2, 100)
data = np.dot(c, x) + 0.1*np.random.randn(10, 100)
Y.observe(data)
Y.observe(data, mask=[[True], [False], [False], [True], [True],[False], [True], [True], [True], [False]])

from bayespy.inference import VB
Q = VB(Y, C, X, alpha, tau)
Q['X']
Q['X'] is X


# Initializing the posterior approximation
X.initialize_from_parameters(np.random.randn(1, 100, D), 10)
Q.update()
Q.update(C, X)
Q.update(C, X, C, tau)
Q.update(repeat=10)
Q.update(repeat=1000)
Q.update(repeat=10000, tol=1e-6)
C.update()
Q['C'].update()


from bayespy.inference.vmp import transformations
rotX = transformations.RotateGaussianARD(X)
rotC = transformations.RotateGaussianARD(C, alpha)
R = transformations.RotationOptimizer(rotC, rotX, D)
R.rotate()
alpha.initialize_from_prior()
C.initialize_from_prior()
X.initialize_from_parameters(np.random.randn(1, 100, D), 10)
tau.initialize_from_prior()
Q = VB(Y, C, X, alpha, tau)
Q.callback = R.rotate
Q.update(repeat=1000, tol=1e-6)


import bayespy.plot as bpplt
bpplt.pyplot.ion()
bpplt.pyplot.figure()
bpplt.pdf(Q['tau'], np.linspace(60, 140, num=100))
V = Gaussian([3, 5], [[4, 2], [2, 5]])
bpplt.pyplot.figure()
bpplt.contour(V, np.linspace(1, 5, num=100), np.linspace(3, 7, num=100))
bpplt.pyplot.figure()

bpplt.hinton(C)
bpplt.pyplot.figure()

bpplt.pyplot.figure()
bpplt.hinton(C)


tau.set_plotter(bpplt.PDFPlotter(np.linspace(60, 140, num=100)))
C.set_plotter(bpplt.HintonPlotter())
X.set_plotter(bpplt.FunctionPlotter(axis=-2))

V = Gaussian([3, 5], [[4, 2], [2, 5]],plotter=bpplt.ContourPlotter(np.linspace(1, 5, num=100),np.linspace(3, 7, num=100)))

V.plot()
Q.plot('C')
Q.update(repeat=5, plot=True, tol=np.nan)

import tempfile
filename = tempfile.mkstemp(suffix='.hdf5')[1]
Q.save(filename=filename)
Q.load(filename=filename)

Q = VB(Y, C, X, alpha, tau)
Q.optimize(C, X, riemannian=False, method='gradient', maxiter=5)
Q.optimize(C, tau, maxiter=10, collapsed=[X, alpha])
Q.pattern_search(C, X)
Q.pattern_search(C, tau, collapsed=[X, alpha])
beta = 0.1
while beta < 1.0:beta = min(beta*1.5, 1.0),Q.set_annealing(beta),Q.update(repeat=100, tol=1e-4)

X = GaussianARD(0, 1,shape=(D,),plates=(1,plates_multiplier=(1,20),name='X')


F = Dot(C, X)
Y = GaussianARD(F, tau, name='Y')
Q = VB(Y, C, X, alpha, tau)
C.initialize_from_random()
Q.ignore_bound_checks = True
for n in range(200):
                subset = np.random.choice(100, 5)
                Y.observe(data[:,subset])
                Q.update(X)
                learning_rate = (n + 2.0) ** (-0.7)
                Q.gradient_step(C, alpha, tau, scale=learning_rate)


bpplt.plot(X, axis=-2)
