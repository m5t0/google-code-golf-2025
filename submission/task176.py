p=lambda g,e=enumerate:[[w or(1-i<-~j%12<i+1or 4+i<j%12<8-i)*4for j,w in e(v)]for i,v in e(g)]



p=lambda g:[[w+(1-i<-~j%12<i+1<4+i<j%12<8-i)*4for j,w in enumerate(g[i])]for i in[0,1,2]]