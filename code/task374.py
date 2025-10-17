def p(g):
 k=0;C='142';n=9
 while k<3:exec("g[:]=zip(*eval(str(g[::-1]).replace('5, '*n,f'{C[k]},'*n)));"*4);k+=C[k]in str(g);n-=1
 return g