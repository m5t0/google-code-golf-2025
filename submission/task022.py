t=-1,0,1
p=lambda g:[[max(s[i+a*11+b]for i in range(121)if(s:=sum(g,[]))[i]==5)for b in t]for a in t]