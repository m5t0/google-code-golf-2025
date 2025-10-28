def p(p):
 n=p[0][0];s=sorted((sum(p,[]).count(f),f)for f in range(10)if f!=n);t=s[-1][1];o=[f for s,f in s if f'{f}, {t}'in str(p) and f!=t][0]
 for f in range(900):
  if p[f//30][f%30]==o:
   e=[s[f%30-1:f%30+2]for s in p[f//30-1:f//30+2]]
   if(t in sum(e,[])or n==e[0][1])^1:
    s=[s[f%30-1:f%30+2]for s in p[f//30-1:f//30+2]]
    for r in range(25):p[f//30-2+r//5][f%30-2+r%5]=n
 s=eval(str(s).replace(str(n),str(t)));e=eval(str(p))
 for f in range(900):
  for r in range((p[f//30][f%30]==o)*9):e[f//30-1+r//3][f%30-1+r%3]=s[r//3][r%3]
 n=[s[0][1],s[1][0]][s[0][1]==s[0][0]];exec(f"e[:]=zip(*eval(str(e).replace('{o}, {n}, {t}','{o},{n},{n}').replace('{n}, {n}, {t}','{n},{n},{n}'))[::-1]);"*60);return e