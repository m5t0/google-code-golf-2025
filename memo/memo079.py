# まだ解けていない
# p=lambda g,r=range(11):[w for i in r for j in r[::-1]if sum(map(sum,(w:=[v[j:j+3]for v in g[i:i+3]])))>3*max(map(max,w))][0]