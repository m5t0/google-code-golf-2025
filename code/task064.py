e=lambda r,m:(len({*(t:=r[:m+1])})>1<len({*r[m:]}))*({*t}!={*r[m:]})
m=lambda r,e=min:e(r,key=r.count)
p=lambda z,n=enumerate:[[[r[n],m(r),m(t)][r[n]==m(z[0],max)and e(r,n)+e(t,p)*2]for n,t in n(zip(*z))]for p,r in n(z)]