golf=lambda p:len(p)>9 and all([any([x.isupper() for x in p]),any([x.islower() for x in p]),any([x.isdigit() for x in p])])
