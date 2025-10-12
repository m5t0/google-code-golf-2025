f=lambda v,I:1in{*v[:I]}&{*v[I:]}and v[:I][::-1].index(1)+v[I:].index(1)
p=lambda g,e=enumerate:[[w[i]or(x:=f(v,j))==f(w,i)>0and 2+x%2*5for j,w in e(zip(*g))]for i,v in e(g)]