import re
def p(e):
 r=re.sub(', ','',str(e+[*zip(*e)]));r+=r[::-1];e=int(max(r,key=r.count));s={0:(0,e)}
 for i in range(10):
  if (i!=e)*(t:=re.findall(f'{i}+',r)):
   o=len(re.findall(f'{i}{i}([^]){i}]+){i}|$',r)[0])
   s[len(max(t))*-~(o>0)+o>>1]=o+1>>1,i
 r=max(s)
 return [[e*((o:=s[max(abs(i),abs(t))])[0]>min(abs(i),abs(t)))or o[1] for i in range(-r,r+1)]for t in range(-r,r+1)]