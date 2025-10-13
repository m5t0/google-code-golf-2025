def p(o):
 f=eval(str(o))
 for a in range(200):
  for a in range(o[(r:=a//100+3)+(e:=a//10%10):]>[]and{*o[e][(s:=a%10):s+r]+o[t:=e+~-r][s:s+r]}=={i:=o[e][s]}!={0}and r*r*3-4*r):f[e+(d:=a//r-r+2)][g:=s+(a:=a%r)]=f[a:=e+a][s+d]=i;f[e][g]=f[t][g]=f[a][s]=f[a][s+~-r]=o[e+1][s+1]
 return f