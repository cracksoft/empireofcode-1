import re
golf = lambda b: sum((ord(x[0])-65)*9+int(x[1]) for x in re.findall('[A-Z][1-9]', b))
