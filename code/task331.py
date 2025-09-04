d=0,1,0,-1
p=lambda g:[exec("g[I][J]=[7,8,6,2][k]")for x in range(100)for k in[0,1,2,3]*(g[x//10][x%10]&1)if-1<(I:=x//10+d[k])<10>(J:=x%10+d[k-1])>=0]and g