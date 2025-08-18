# 色々減らした
def p(g,r=range):f=lambda x:min(i for i in r(19)if min(x[i:i+3]));s,t=f([*map(m:=max,g)]),f([*map(m,zip(*g))]);h=lambda x:4*((x>0)-(x<0));return[[m(g[s+h(x:=(i-s)//4)+k//3][t+h(y:=(j-t)//4)+k%3]for k in r(9))*(g[s+(i-s)%4][t+(j-t)%4]>0)*((x*x==y*y)|(x*y==0))for j in r(21)]for i in r(21)]
# 変数a,bを削除
def p(g):r,f=range,lambda x:min((i for i in r(19)if all(x[i:i+3])));s,t=f([*map(any,g)]),f([*map(any,zip(*g))]);return[[max([g[min(20,max(0,s+4*((x>0)-(x<0))+k//3))][min(20,max(0,t+4*((y>0)-(y<0))+k%3))]for k in r(9)])*(g[s+(i-s)%4][t+(j-t)%4]>0)if abs(x:=(i-s)//4)==abs(y:=(j-t)//4)or x*y==0 else 0 for j in r(21)]for i in r(21)]
# 同じ処理をする箇所をラムダ式に変更
def p(g):r,a,b=range,[*map(any,g)],[*map(any,zip(*g))];f=lambda x:min((i for i in r(19)if all(x[i:i+3])));s,t=f(a),f(b);return[[max([g[min(20,max(0,s+4*((x>0)-(x<0))+k//3))][min(20,max(0,t+4*((y>0)-(y<0))+k%3))]for k in r(9)])*(g[s+(i-s)%4][t+(j-t)%4]>0)if abs(x:=(i-s)//4)==abs(y:=(j-t)//4)or x*y==0 else 0 for j in r(21)]for i in r(21)]
# list()を[*]に変更
def p(g):r,a,b=range,[*map(any,g)],[*map(any,zip(*g))];s,t=min((i for i in r(19)if all(a[i:i+3]))),min((j for j in r(19)if all(b[j:j+3])));return[[max([g[min(20,max(0,s+4*((x>0)-(x<0))+k//3))][min(20,max(0,t+4*((y>0)-(y<0))+k%3))]for k in r(9)])*(g[s+(i-s)%4][t+(j-t)%4]>0)if abs(x:=(i-s)//4)==abs(y:=(j-t)//4)or x*y==0 else 0 for j in r(21)]for i in r(21)]
# 更に空白を埋めたコード
def p(g):r,a,b=range,list(map(any,g)),list(map(any,zip(*g)));s,t=min((i for i in r(19)if all(a[i:i+3]))),min((j for j in r(19)if all(b[j:j+3])));return[[max([g[min(20,max(0,s+4*((x>0)-(x<0))+k//3))][min(20,max(0,t+4*((y>0)-(y<0))+k%3))]for k in r(9)])*(g[s+(i-s)%4][t+(j-t)%4]>0)if abs(x:=(i-s)//4)==abs(y:=(j-t)//4)or x*y==0 else 0 for j in r(21)]for i in r(21)]
# 配列cを削除してxやyの条件を整理したコード
def p(g):r,a,b=range,list(map(any,g)),list(map(any,zip(*g)));s,t=min((i for i in r(19)if all(a[i:i+3]))),min((j for j in r(19)if all(b[j:j+3])));return [[max([g[min(20,max(0,s+4*((x>0)-(x<0))+k//3))][min(20,max(0,t+4*((y>0)-(y<0))+k%3))]for k in r(9)])*(g[s+(i-s)%4][t+(j-t)%4]>0)if abs(x:=(i-s)//4)==abs(y:=(j-t)//4)or x*y==0 else 0 for j in r(21)]for i in r(21)]
# 内包表記によるコード
def p(g):r,d,a,b=range,[-4,0,4],list(map(any,g)),list(map(any,zip(*g)));s,t=min((i for i in r(19)if all(a[i:i+3]))),min((j for j in r(19)if all(b[j:j+3])));c=[[max([g[min(20,max(0,s+i+k//3))][min(20,max(0,t+j+k%3))] for k in r(9)])for j in d]for i in d];return [[c[(x>=0)+(x>0)][(y>=0)+(y>0)]*(g[s+(i-s)%4][t+(j-t)%4]>0)if(p:=abs(x:=(i-s)//4))==(q:=abs(y:=(j-t)//4))or min(p,q)==0 else 0 for j in r(21)]for i in r(21)]

# whileではなくて数回やればいいという発想になったが保留
#  for i in d:
#   for j in d:
#    for p in r(6):
#     for k in r(9):
#      if 0<=s+i*p+k//3<21 and 0<=t+j*p+k%3<21:g[s+i*p+k//3][t+j*p+k%3]=max([g[s+i+m//3][t+j+m%3]for m in r(9) if 0<=s+i+m//3<21 and 0<=t+j+m%3<21])*(g[s+k//3][t+k%3]>0)
#  return g

# for文で愚直に書くコード
# 端っこの部分で間違っている
def p(g):
    r,d,a,b=range,[-4,0,4],list(map(any, g)),list(map(any, zip(*g)));s,t=min((i for i in r(19) if all(a[i:i+3]))),min((j for j in r(19) if all(b[j:j+3])))
    for i in d:
        for j in d:
            if i==0 and j==0: continue
            x,y=s,t
            while (x:=x+i)>=0 and x<19 and (y:=y+j)>=0 and y<19:
                for k in r(9):g[x+k//3][y+k%3]=max([g[s+i+m//3][t+j+m%3] for m in r(9)])*(g[s+k//3][t+k%3]>0)
    return g

from pprint import *
pprint(
    p(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 8, 8, 8, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 8, 0, 8, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 8, 8, 8, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
)