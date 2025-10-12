def p(e):
 for f,i in enumerate(e):
  if 5in i:m=i.index(5);break
 else:return 1
 if[5]==i[m+1:m+2]and e[f+1][m:m+2]==[5,5]:
  i[m:m+2]=e[f+1][m:m+2]=8,8
  if p(e):return e
  i[m:m+2]=e[f+1][m:m+2]=5,5
 if i[m+1:m+3]==[5,5]:
  i[m:m+3]=2,2,2
  if p(e):return e
  i[m:m+3]=5,5,5
 if f<6and e[f+1][m]==e[f+2][m]==5:
  i[m]=e[f+1][m]=e[f+2][m]=2
  if p(e):return e
  i[m]=e[f+1][m]=e[f+2][m]=5