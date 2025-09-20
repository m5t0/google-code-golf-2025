f=lambda g:[*filter(None,{}.fromkeys(max(g,key=g.count)))]
p=lambda g:max(len(x:=f(g))*[x],[*zip(*(len(y:=f([*zip(*g)]))*[y]))],key=len)