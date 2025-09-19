def p(p,R=range):
 a=sum(p,e:=[]);p=[];n=[[]];r=15
 for i in R(16):
  if(5in a[i::r])>i/r:p+=[i]
  elif p:i=[n for n in R(150)if a[n]>4and n%r in p];e+=[[n-i[0]for n in i]];p=[];n=[i+[n]for i in n for n in R(45)if 1>a[n]]
 for i in n:
  i=[any(n-i in e*(6>i%r-n%r)for i,e in zip(i,e))|a[n]%5for n in R(150)]
  if all(i[:45])*(i.count(0)==a.count(0)):return[i[n*r:][:r]for n in R(10)]

def p(p):
 # pには列番号を入れる
 # 5が連続して入るような列番号を取ってくる
 a=sum(p,e:=[]);p=[];n=[[]];r=15
 for i in range(16):
  # 5がi列目に含まれる場合にiをpに追加する(ただし、右端は除外する)
  if(5in a[i::r])>i/r:p+=[i]
  # 右端、またはi列目に5が存在しない場合
  elif p:
   # 値が5で列番号がpに含まれるような座標を取ってくる
   i=[n for n in range(150)if a[n]>4and n%r in p]
   # pの中で一番左上から見た相対座標を見る
   e+=[[n-i[0]for n in i]]
   # pを初期化する
   p=[]
   n=[i+[n]for i in n for n in range(45)if 1>a[n]]
 # nは0のブロックの左上の座標を全探索したもの
 # nのshapeは(0のブロックのマスの個数)^(0のブロックの個数)x(0のブロックの個数)
 for i in n:
  # 下のコードにおける変数
  # n:マスの座標
  # i:0のブロックの中の座標
  # e:5のブロックの中の相対座標のリスト
  # a[n]=2または(0のブロックのマスの列座標-マスの列番号<6)で
  # 0のブロックと5のブロックの配置が同じ
  i=[any(n-i in e*(6>i%r-n%r)for i,e in zip(i,e))|a[n]%5for n in range(150)]
  # 3行目まで全部色がついていて色がついていないマスの個数がaとiで同じ
  if all(i[:45])*(i.count(0)==a.count(0)):return[i[n*r:][:r]for n in range(10)]

def p(g,e=enumerate):
 s=[];t=[];z=(0,)*7
 for y in [*zip(*g[3:])]+[z]:
  t+=(y!=z)*[y]
  if y==z and t:s+=[list(filter(any,zip(*t)))];t=[]
 g[3:]=[[0]*len(v)for v in g[3:]]
 for h in s[::-1]:
  t=1;k=h[0].index(5)
  for i,v in e(g[:3]):
   for j,w in e(v):
    if t and w<1and str(g[2])[1::3].find('2',j)%16<=j-k+len(h[0])<16and g[i-1][j]and(j<1 or v[j-1])and all(i+m>2or (b>0)^(g[i+m][j-k+n]>0)for m,a in e(h)for n,b in e(a)):
     for m,a in e(h):
      for n,b in e(a):g[i+m][j-k+n]+=b>0
     t=0
 return g