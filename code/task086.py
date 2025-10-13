def p(o):
 f=eval(str(o))
 for a in range(200):
  for a in range(o[(r:=a//100+3)+(e:=a//10%10):]>[]and{*o[e][(p:=a%10):p+r]+o[t:=e+~-r][p:p+r]}=={i:=o[e][p]}!={0}and r*r*3-4*r):f[e+(d:=a//r-r+2)][v:=p+(a:=a%r)]=f[a:=e+a][p+d]=i;f[e][v]=f[t][v]=f[a][p]=f[a][p+~-r]=o[e+1][p+1]
 return f