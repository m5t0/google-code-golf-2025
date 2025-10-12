f=lambda v,i:max(((s:=(str(v)[1::3])).rfind("8",0,i+k)-s.rfind("2",0,i+k))*(s.find("8",i+k)%(l:=1+len(v))-s.find("2",i+k)%l)for k in[0,1])>0
def p(g,e=enumerate):
 h=eval(str(g))
 s=set()
 for i,v in e(g):
  for j,w in e(zip(*g)):
   h[i][j]+=f(w,i)+f(v,j)
   if h[i][j]>8:
    h[i][j]=2
    for k in range(9):
     if k!=4:s.add((i-1+k//3,j-1+k%3))
 return[[((i,j)in s and 8)or(w[i]>0)*(w[i]//8*6+2)for j,w in e(zip(*h))]for i,v in e(h)]