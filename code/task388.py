def p(g):
 r=range((s:=len(g))*2)
 return[[[g[I:=i%s][J:=j%s],[8,g[I][J]][g[I][J]>0]][bool(set([*zip(*g)][J])-{0})]for j in r]for i in r]