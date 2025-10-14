def p(f,o=range):
 i=f[0][0];s=sorted((sum(f,[]).count(r),r)for r in o(10)if r!=i);u=s[-1][1];s=[r for o,r in s if f'{r}, {u}'in str(f) and r!=u][0]
 for r in o(900):
  if f[r//30][r%30]==s:
   d=[e[r%30-1:r%30+2]for e in f[r//30-1:r//30+2]]
   if(u in sum(d,[])or i==d[0][1])^1:
    e=[e[r%30-1:r%30+2]for e in f[r//30-1:r//30+2]]
    for t in o(25):f[r//30-2+t//5][r%30-2+t%5]=i
 e=eval(str(e).replace(str(i),str(u)));d=eval(str(f))
 for r in o(900):
  for t in o((f[r//30][r%30]==s)*9):d[r//30-1+t//3][r%30-1+t%3]=e[t//3][t%3]
 i=[e[0][1],e[1][0]][e[0][1]==e[0][0]];exec(f"d[:]=zip(*eval(str(d).replace('{s}, {i}, {u}','{s},{i},{i}').replace('{i}, {i}, {u}','{i},{i},{i}'))[::-1]);"*60);return d