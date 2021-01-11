'''
Created on Nov 27, 2020

@author: Salzaidy
'''

# create new dict and loop throgh the array
# check if the number exists in the dict increment by 1
#  if not append the number to the dict
def find_it(seq):
    
    newDict = {}
     
    for num in seq:
        if num in newDict.keys():
            newDict[num] += 1
        else:
            newDict[num] = 1
    print(newDict)
    
    for key, value in newDict.items():
        if value % 2 != 0:
            return key
    
    
s = find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
print(s)