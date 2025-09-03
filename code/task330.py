d=0,1,0,-1
def D(g,i,j,P):
 if(0<=i<10>j>=0)^1or P-g[i][j]!=1:return 0
 g[i][j]+=1;return 1+sum(D(g,i+d[I],j+d[I-1],g[i][j])for I in[0,1,2,3])
p=lambda g,r=range(10):[[[x:=g[i][j],1+(D(g,i,j,x+(x>0))==6)][x>0]for j in r]for i in r]