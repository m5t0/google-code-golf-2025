from itertools import*
f=lambda s:[k for k,_ in groupby(s)];p=lambda g:max([f(g[0])],[[v]for v in f([*zip(*g)][0])])