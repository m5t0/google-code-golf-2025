import re
def p(e):
 r=re.sub(', ','',str(e+[*zip(*e)]));r+=r[::-1];e=int(max(r,key=r.count));f={0:(0,e)}
 for n in range(10):
  if (n!=e)*(i:=re.findall(f'{n}+',r)):
   p=len(re.findall(f'{n}{n}([^]){n}]+){n}|$',r)[0])
   f[len(max(i))*-~(p>0)+p>>1]=p+1>>1,n
 r=max(f)
 return [[e*((p:=f[max(abs(n),abs(i))])[0]>min(abs(n),abs(i)))or p[1] for n in range(-r,r+1)]for i in range(-r,r+1)]