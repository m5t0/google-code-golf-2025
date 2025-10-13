d=lambda v,l:max(((t:=(str(v)[1::3])).rfind("8",0,l+a)-t.rfind("2",0,l+a))*(t.find("8",l+a)%(d:=1+len(v))-t.find("2",l+a)%d)for a in[0,1])>0
def p(g,p=enumerate):
 i=eval(str(g))
 t=set()
 for l,v in p(g):
  for e,u in p(zip(*g)):
   i[l][e]+=d(u,l)+d(v,e)
   if i[l][e]>8:
    i[l][e]=2
    for a in range(9):
     if a!=4:t.add((l-1+a//3,e-1+a%3))
 return[[((l,e)in t and 8)or(u[l]>0)*(u[l]//8*6+2)for e,u in p(zip(*i))]for l,v in p(i)]