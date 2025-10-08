def p(g):
 for _ in[0]*88:
  if(v:=[i for i,v in enumerate(g)if all(v)]):g[:max(v)]=[*zip(*eval(str([*zip(*g[:max(v)])]).replace("2, 0","2, 2")))]
  g=[*map(list,zip(*g))][::-1]
 h=eval(str(g))
 for i,v in enumerate(g):
  for j,w in enumerate(zip(*g)):
   if v[j]==8and 2in v[j-(j>0):j+2]+[*w[i-(i>0):i+2]]:
    for a in h[i-1:i+2]:a[j-1:j+2]=[8]*3
    h[i][j]=2
 return h