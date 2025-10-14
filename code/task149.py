s=0,4,8
p=lambda j:[[sum(r[k:k+3].count(6)for r in j[e:e+3])>1for k in s]for e in s]