def p(a,z=range):
 f,d=len(a),len(a[0]);r,*k=[],
 for q in z(f*d):
  if a[l:=q//d][h:=q%d]==2:
   r+=(e:={(0,0)}),;k+=(l,h),
   for q in z(50):e|={(j,m)for r,o in e for q in z(9)if d>h+(m:=o+q%3-1)>=0<f>l+(j:=r+q//3-1)>=0<a[l+j][h+m]}
 o,h=k[r.index(e:=max(r,key=len))];p=e
 for g,(l,f)in zip(r,k):
  for q in z(-3,5):
   if g<{*e}and all(((r,q)in g)<=(a[l+r][f+q]==a[o+j][h+m])for(r,q),(j,m)in zip(e,p)):
    for(r,q),(j,m)in zip(e,p):a[l+r][f+q]=a[o+j][h+m]
   e=[(-q,r)for r,q in e];q or(e:=[(-r,q)for r,q in e])
 return a