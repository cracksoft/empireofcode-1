def golf(c,t=0):
 k=[]   
 for x in c:
  y=len(x)
  if y>4:
   k.append(int(x[5:]))
  else:
   t+=(k.pop() if y<4 else k[-1]) if k else 0
 return t
