e=enumerate
def p(g):g=[[w[i]*(w[i]in{*v[j-1:j+2:2]}&{*w[i-1:i+2:2]})for j,w in e(zip(*g))]for i,v in e(g)];return[[x*(sum(g,[]).count(x)>6)for x in v]for v in g]