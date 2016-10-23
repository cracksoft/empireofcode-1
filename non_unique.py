def non_unique(data):
    return [i for i in data if 
            (str(i).isalpha() and (data.count(i.upper()) > 1 or data.count(i.lower()) > 1)) or data.count(i) > 1]
