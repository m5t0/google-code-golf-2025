def p(s):
 f=eval(str(s))
 for a in range(200):
  for a in range(s[(r:=a//100+3)+(e:=a//10%10):]>[]and{*s[e][(g:=a%10):g+r]+s[u:=e+~-r][g:g+r]}=={l:=s[e][g]}!={0}and r*r*3-4*r):f[e+(d:=a//r-r+2)][t:=g+(a:=a%r)]=f[a:=e+a][g+d]=l;f[e][t]=f[u][t]=f[a][g]=f[a][g+~-r]=s[e+1][g+1]
 return f