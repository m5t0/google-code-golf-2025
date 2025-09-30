from itertools import*
p=lambda g:[*accumulate([v+[0]*3for v in g]+[[0]*6]*3,lambda a,b:[*map(sum,zip([0]+a,b))])]