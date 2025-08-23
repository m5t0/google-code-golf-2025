def p(g,r=range(10)):f=lambda h,x=[*zip(*g)]:h(i for i in r if max(x[i]));a,d=f(min,g),f(max);c=min(d-f(max,g)+a,f(min));return[[g[i][j]or(0<=a+j-c<10>a+d-i>=0)*1and(g[a+j-c][a+d-i]>0)*2for j in r]for i in r]

def p(g,r=range(10)):f=lambda h,x=[*zip(*g)]:h(i for i in r if max(x[i]));a,d=f(min,g),f(max);c=d-max(f(max,g)-a,d-f(min));return[[g[i][j]or(0<=a+j-c<10>a+d-i>=0)*1and(g[a+j-c][a+d-i]>0)*2for j in r]for i in r]

def p(g,r=range(10)):f=lambda x=[*zip(*g)]:(i for i in r if any(x[i]));a,d=min(f(g)),max(f());l=max(max(f(g))-a,d-min(f()));b=a+l;c=d-l;return[[1*(0<=a+j-c<10>c+b-i>=0)and(g[i][j]or(g[a+j-c][c+b-i]>0)*2)for j in r]for i in r]

def p(g,r=range):
 r,f=range(10),lambda x=[*zip(*g)]:(i for i in r if any(x[i]));a,d=min(f(g)),max(f());l=max(max(f(g))-a,d-min(f()))+1;c=d-l+1
 return[[1*(0<=a+j-c<10>c+a+l-i-1>=0)and(g[i][j]or(g[a+j-(d-l+1)][(d-l+1)+a+l-i-1]>0)*2)for j in r]for i in r]