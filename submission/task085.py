p=lambda g,e=enumerate:[exec("g[i][j]=0")for i,v in e(g)for j,w in e(v)if len({*str([*zip(*g[i-1:i+2])][j-1:j+2])})==7]and g




p=lambda g,e=enumerate:[[w[i]and(len({*w[i-1:i+2]})>1)*w[i]or([*v,0].index(0)-j-1)%2*w[i]for j,w in e(zip(*g))]for i,v in e(g)]