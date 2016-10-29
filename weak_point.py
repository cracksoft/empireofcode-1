def golf(m):
 r = sorted([(sum(m[i]),i) for i in range(len(m))]) 
 m = list(zip(*m))
 x = sorted([(sum(m[i]),i) for i in range(len(m))])
 return [r[0][1], x[0][1]]
