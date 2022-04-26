dict1 = {'a': 10, 'b':20, 'c':30}
dict2 = {'a': 10, 'c':20, 'd':30, 'e':40}
dict3 = {**dict1,**dict2}
for key1, value1 in dict1.items():
    for key2, value2 in dict2.items():
        if key1 == key2:
            dict3[key1]=(value1+value2)    
print(dict3)
