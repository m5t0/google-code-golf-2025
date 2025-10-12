def p(o,r=range):
 e=o[0][0];s=sorted((sum(o,[]).count(i),i)for i in r(10)if i!=e);d=s[-1][1];c=[i for p,i in s if f'{i}, {d}'in str(o) and i!=d][0]
 for i in r(900):
  if o[i//30][i%30]==c:
   f=[p[i%30-1:i%30+2]for p in o[i//30-1:i//30+2]]
   if(d in sum(f,[])or e==f[0][1])^1:
    p=[p[i%30-1:i%30+2]for p in o[i//30-1:i//30+2]]
    for n in r(25):o[i//30-2+n//5][i%30-2+n%5]=e
 p=eval(str(p).replace(str(e),str(d)));f=eval(str(o))
 for i in r(900):
  for n in r((o[i//30][i%30]==c)*9):f[i//30-1+n//3][i%30-1+n%3]=p[n//3][n%3]
 e=[p[0][1],p[1][0]][p[0][1]==p[0][0]];exec(f"f[:]=zip(*eval(str(f).replace('{c}, {e}, {d}','{c},{e},{e}').replace('{e}, {e}, {d}','{e},{e},{e}'))[::-1]);"*60);return f