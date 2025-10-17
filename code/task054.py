def p(r,e=range):
 o=r[0][0];s=sorted((sum(r,[]).count(f),f)for f in e(10)if f!=o);n=s[-1][1];p=[f for s,f in s if f'{f}, {n}'in str(r) and f!=n][0]
 for f in e(900):
  if r[f//30][f%30]==p:
   t=[s[f%30-1:f%30+2]for s in r[f//30-1:f//30+2]]
   if(n in sum(t,[])or o==t[0][1])^1:
    s=[s[f%30-1:f%30+2]for s in r[f//30-1:f//30+2]]
    for d in e(25):r[f//30-2+d//5][f%30-2+d%5]=o
 s=eval(str(s).replace(str(o),str(n)));t=eval(str(r))
 for f in e(900):
  for d in e((r[f//30][f%30]==p)*9):t[f//30-1+d//3][f%30-1+d%3]=s[d//3][d%3]
 o=[s[0][1],s[1][0]][s[0][1]==s[0][0]];exec(f"t[:]=zip(*eval(str(t).replace('{p}, {o}, {n}','{p},{o},{o}').replace('{o}, {o}, {n}','{o},{o},{o}'))[::-1]);"*60);return t