def p(g):
 import numpy as np
 return np.kron(g, np.ones((3, 3))).tolist()
