s="g[:]=zip(*eval(str(g).replace('%s'))[::-1]);"
p=lambda g:exec(s%"0','3"*4+s%"3, 3','2,2"*4+s%"2, 3','1,1"*4+s%"1, 2','1,1"*4)or g