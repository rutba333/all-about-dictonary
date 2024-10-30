#initialize dictonary 
test_dict={'codingal':2,'is': 2, 'best':2,'for' :2,'codingal':2}
#printing original dictonary
print("The original dictonary:"+ str(test_dict))
#initialize value
K=2
#using loop
#selective key values in dictonary
res=0

for key in test_dict:
    if test_dict[key]==K:
        res=res+1

#printing the result
print("Frequency of K is:"+ str(res))





