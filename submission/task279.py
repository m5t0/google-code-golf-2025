def D(g,i,j,d):
 if len(g)>i>-1<j<len(v:=g[i]):
  if v[j]%9:v[j]^=1;s=max(D(g,i+I//3,~-j+I%3,I)or 0for I in[-2,0,2,4]if I+d-2);v[j]^=1;return s
  return(v[j]<9)*7
p=lambda g,e=enumerate:[[D(g,i,j,1)+v[j]for j,_ in e(zip(*g))]for i,v in e(g)]