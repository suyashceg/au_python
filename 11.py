def abbr(name):
    lst = name.split(' ')
    
    lst2 = []
    for i in lst:
        
        lst2.append(i[0])
    
    return ''.join(map(str,lst2)).upper()

print(abbr("Gautam Gambhir"))

