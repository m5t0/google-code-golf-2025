def p(a):
 f=eval(str(a))
 for t in range(200):
  for t in range(a[(r:=t//100+3)+(e:=t//10%10):]>[]and{*a[e][(d:=t%10):d+r]+a[n:=e+~-r][d:d+r]}=={o:=a[e][d]}!={0}and r*r*3-4*r):f[e+(s:=t//r-r+2)][u:=d+(t:=t%r)]=f[t:=e+t][d+s]=o;f[e][u]=f[n][u]=f[t][d]=f[t][d+~-r]=a[e+1][d+1]
 return f