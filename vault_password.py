golf=lambda p:len(p)>9 and all(any(map(t, p)) for t in (str.isupper,str.islower,str.isdigit))
