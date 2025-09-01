def p(g,e=enumerate):
 d=0,1,0,-1,0;f=lambda f,g,n,P:1+sum(f(f,g,(I,J),n)for i in range(4)if-1<(I:=n[0]+d[i])<10>(J:=n[1]+d[i+1])>=0and g[I][J]==0and(I,J)!=P)
 return[[w or 4-f(f,g,(i,j),(i,j))for j,w in e(v)]for i,v in e(g)]