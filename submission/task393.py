from collections import*
p=lambda g:[[x]for x,_ in Counter(sum(g,[])).most_common()[1:]]