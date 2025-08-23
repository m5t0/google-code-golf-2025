import base64,zlib;exec(zlib.decompress(base64.b64decode('eJyVkM0KgzAQhO8+xR6VUqgBobR67RP0FnIQjCGi2xLr+zc/axPQg73NDjPLt9vJHt65Km4ZYDNKtPI+BcEvosigfxnQoBFMi0rm6JLeHKI5eRN0D4prwQfRNJV3nKVrPJfQYgdDPZGysVMZgqFhJy+96wda8NsYK7GRFq4hrukcIz+LQVD/LalWaIfKVtSEz0m2TxfXUYgdJNoUq/R1bOdhNpQ+ef88Ch2l2BQDBeUf7TjLbJ2eZpFfTZCl0A==')))

# decompress
def p(g):
 n=len(g);m=len(g[0])
 for i in range(n):
  for j in range(m):
   if g[i][j]==5:
    if i<n-1 and j<m-1 and g[i+1][j]==g[i][j+1]==g[i+1][j+1]==5:
     g[i][j]=g[i+1][j]=g[i][j+1]=g[i+1][j+1]=8
     if p(g):return g
     g[i][j]=g[i+1][j]=g[i][j+1]=g[i+1][j+1]=5
    if j<m-2 and g[i][j+1]==g[i][j+2]==5:
     g[i][j]=g[i][j+1]=g[i][j+2]=2
     if p(g):return g
     g[i][j]=g[i][j+1]=g[i][j+2]=5
    if i<n-2 and g[i+1][j]==g[i+2][j]==5:
     g[i][j]=g[i+1][j]=g[i+2][j]=2
     if p(g):return g
     g[i][j]=g[i+1][j]=g[i+2][j]=5
    return False
 return True