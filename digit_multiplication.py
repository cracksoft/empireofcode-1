def golf(x):
 t = 1
 for i in str(x):
  t *= max(int(i),1)
 return t
