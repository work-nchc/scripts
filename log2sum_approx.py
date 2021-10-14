from scipy.optimize import fmin
from numpy import log2
#from sys import float_info
#t = float_info.min
t = 2 * 10**-16

def h(y):
    f = lambda x: log2(1+0.5**x) - y**x
    a = fmin(f, 2, xtol=t, ftol=t, disp=0)
    g = lambda x: y**x - log2(1+0.5**x)
    b = fmin(g, 2, xtol=t, ftol=t, disp=0)
    return -min(f(a), g(b))

c = fmin(h, 0.57, xtol=t, ftol=t)
hc = h(c)
print(t, c[0], 2 ** hc[0])

'''
Warning: Maximum number of function evaluations has been exceeded.
2.2250738585072014e-308 0.5695214295324008 1.0123855787133282

Warning: Maximum number of function evaluations has been exceeded.
1e-16 0.5695214295324008 1.0123855787133282

Optimization terminated successfully.
         Current function value: 0.017759
         Iterations: 46
         Function evaluations: 92
1e-15 0.5695214295324011 1.0123855787133282

Optimization terminated successfully.
         Current function value: 0.017759
         Iterations: 49
         Function evaluations: 98
2e-16 0.5695214295324008 1.0123855787133282
'''
