p=lambda g,r=range(17):[[[v[j],3][v[j]<2and min(x:=[k for k in r if 8in[*zip(*g)][k]])<=j<=max(x)and 8in v]for j in r]for v in g]


p=lambda g,e=enumerate:[[[w[i],(8in{*w[i-1:i]+w[i+1:i+2]})*2+1][w[i]&1]for j,w in e(zip(*g))]for i,v in e(g)]