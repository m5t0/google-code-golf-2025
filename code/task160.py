r=range
p=lambda g:any(exec("g[k//8+l//3][k%8+l%3]=2*(1in(l//3,l%3))")for k in r(64)if all(g[k//8+m//3][k%8+m%3]==(m!=4)for m in r(9))for l in r(9))or g