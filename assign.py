'''
Python program to find smallest number in a list
Using function 
Input : list1 = [5, 7, 9, 14, 10, 20, 4] 
Output : 4
'''

def sum_list(li):
    sm = li[0]
    for i in li:
        if i < sm:
            sm = i
    return sm
li = [5, 7, 9, 14, 10, 20, 4]
print(sum_list(li))
