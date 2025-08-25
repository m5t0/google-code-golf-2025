import base64,zlib;exec(zlib.decompress(base64.b64decode('eNp9jt0KwjAMhe/3FLncWBG2URnVPknpxWTZaNUqcQMf3+wPJzoJgXBy+M6psYF73CYqguZG4ARvAAz9FanqcPqAa0CyTMpr2rlQ4zOWyeFEWJ0jwMsDFWHXU4AsYq+RVmsyPs2UT3NbhRpa49LMGj8KWhsppB3AtEifhlKUU+pYbWa3237GDcGwhBbfGSzlgucftxhJM8sd9+vmTBzOfDrlDH4Xsav3dshvv3wBaLZxwA==')))

# decompress
def p(g):
 for i,r in enumerate(g):
  if 5in r:j=r.index(5);break
 else:return 1
 if[5]==r[j+1:j+2]and g[i+1][j:j+2]==[5,5]:
  r[j:j+2]=g[i+1][j:j+2]=8,8
  if p(g):return g
  r[j:j+2]=g[i+1][j:j+2]=5,5
 if r[j+1:j+3]==[5,5]:
  r[j:j+3]=2,2,2
  if p(g):return g
  r[j:j+3]=5,5,5
 if i<6and g[i+1][j]==g[i+2][j]==5:
  r[j]=g[i+1][j]=g[i+2][j]=2
  if p(g):return g
  r[j]=g[i+1][j]=g[i+2][j]=5