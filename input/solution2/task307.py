def p(g):
 import numpy as np
 return np.kron(g, np.ones((2, 2))).tolist()
