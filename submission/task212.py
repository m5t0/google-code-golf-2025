f=lambda g:[(t:=0)or[(t:=[[t,s:=2-(t==5)][x==s],5][x>4])%5or x for x in v[::-1]]for v in g]
p=lambda g:[*zip(*f(f(zip(*g))))]