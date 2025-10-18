a="g[:]=zip(*eval(str(g).replace('%s))[::-1]);"
p=lambda g:exec(a%"2','1',2"+a%"2, 1','1,1'"+a%"8, 1','1,1'"*30+a%"1, 2','9'"*8)or[[('9'in str(g))*8]]