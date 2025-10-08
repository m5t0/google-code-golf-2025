import re
def p(g):
 for _ in[0]*88:
  if(v:=[i for i,v in enumerate(g)if all(v)]):g[:max(v)]=[*zip(*eval(re.sub("2, 0","2, 2",str([*zip(*g[:max(v)])]))))]
  g=[*zip(*g)][::-1]
 exec("g[:]=zip(*eval(re.sub('2, 8, 0','5,2,5',str(g)))[::-1]);"*4+"g[:]=zip(*eval(re.sub('[08], 5, [08]','8,8,8',str(g)))[::-1]);"*4);return g