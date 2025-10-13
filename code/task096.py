import re
def p(i):
 n=re.sub(', ','',str(i+[*zip(*i)]));n+=n[::-1];i=int(max(n,key=n.count));f={0:(0,i)}
 for t in range(10):
  if(t!=i)*(e:=re.findall(f'{t}+',n)):d=len((re.findall(f'{t}{t}([^]){t}]+){t}|$',n))[0]);f[len(max(e))*((d>0)+1)+d>>1]=d+1>>1,t
 return[[i*((d:=f[n[1]])[0]>n[0])or d[1]for t in range(-max(f),max(f)+1)if(n:=sorted((abs(t),abs(e))))]for e in range(-max(f),max(f)+1)]