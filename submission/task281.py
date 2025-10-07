e=enumerate
f=lambda g,i:((I:=[i for i,v in e(g)if sum(v)])[0]-i)*(i-I[-1])
p=lambda g:[[sorted({*(V:=sum(g,[]))}-{8},key=V.count)[f(g,i)*(t:=f(zip(*g),j))<1]*(f(g,i)>-1<t)for j,w in e(v)]for i,v in e(g)]