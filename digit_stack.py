def golf(c,t=0):
 k=[]
 for x in c:
  y=x.split()
  if y[0]=="PUSH":
   k.append(int(y[1]))
  elif y[0]=="POP":
   t+=k.pop() if len(k)>0 else 0
  else:
   t+=k[len(k)-1] if len(k)>0 else 0
 return t
