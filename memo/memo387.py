import base64,zlib;exec(zlib.decompress(base64.b64decode("eNpVT0FuwyAQvPsVXFJhea2EWG4r0n0J4oBdjIgbEiGT+NS3l7VrRTmx7MzszHzbgd24g4jRBGdLWbCEh1PAHxu4Kws2XCPzzAcWeSCU+YERdpeozgt6hplwG9LFRjNZ7pTXZabNu1aXiEdSMQMd3mkgyUiCAwg4QgMtvMMHfEqnJom+Gvf7phZamWrc0YB0TnX6lPH8vmyN3i72a0QBXW2WmBT09+ID72lV9+WbkKum6jW2xUJg6Uus5JcbSSJ/5H7zsp639pnv1EyuVEw1un4oof/dnnZpMyM0m2U+Pj/dYh7tlGJg7g8cx24R")))

# decompressed
def p(g,r=range):
 u=0;n=len(g)
 for i in r(n):
  if len(v:=[j for j,x in enumerate(g[i])if x%5])==2:
   a,b=v
   for k in 0,1,2,3,5,6,7,8:g[t:=i+k//3-1][a+k%3-1]=g[i][b];g[t][b+k%3-1]=g[i][a]
   for c in r(1,b-a):
    if~min(c,b-a-c)&1:g[i][a+c]=5
   if u<1:
    for c in r(1,u:=(w:=[x for x in r(n)if g[x][a]%5])[3]-w[1]):
     if~min(c,u-c)&1:g[w[1]+c][a]=g[w[1]+c][b]=5
 return g