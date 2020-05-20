#Get the key corresponding to the minimum value from the following
#dictionary using appropriate python logic
dict= {'physics':'88', 'chemistry':'75', 'maths': '72', 'Basic electrical': '89' }
key_min = min(dict.keys(), key=(lambda k: dict[k]))
print('Minimum Value: ',dict[key_min])

