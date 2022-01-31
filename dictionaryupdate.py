def checkKey(dict, key):
       
    if key in dict.keys():
        print("Key exist, ", end =" ")
        dict.update({'m':600})
        print("value updated =", 600)
    else:
        print("Not Exist")
dict = {'m': 700, 'n':100, 't':500}
   
key = 'm'
checkKey(dict, key)
print(dict)
