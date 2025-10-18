f=lambda g:[(t:=0)or[(t:=[[[t,2][x==2],5-4*(x==1)][t>4],5][x>4])%5or x for x in v[::-1]]for v in g]
p=lambda g:[*zip(*f(f(zip(*g))))]