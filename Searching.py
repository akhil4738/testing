"""
Finding whether a particular element exists in a collection and , if it exists , 
finding its position 

1. Linear search
2. Binary Search 

1. Linear Search : 

> it  checks elements on eby one from beginning to the end until the
 required element is found 


num=[10,20,30,40,50]
target=30
for i in range(len(num)):
    if num[i]==target:
        print("element is found at index",i)
        break
else:
    print("Element not found")

i=0
num[0]==target      X
num[1]==target      X
num[2]==target  : 
def linearch_search(arr , key ):
    for  i in range(len(arr)):
        if arr[i]==key:
            return i 
    return -1
num=[10,20,30,40,50]
target=int(input("enter an element to search "))
result=linearch_search(num, target)

if result != -1:
    print("Found at Index ", result)
else:
    print("element is not found")

    

    num=[10,20,30,40,50,60,70]
key = 50
low=0 
high=len(num)-1
while low <=high :
    mid=(low+high)//2

    if num[mid]==key:
        print("element is found at index ", mid)
        break
    elif key >num[mid]:
        low=mid+1
    else:
        high=mid-1
else:
    print("element is not found")
"""








    







# 100 230 250 270  290 310 330 350 370  







