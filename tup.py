"""
collection of elements of different types 
> ordered 
> immutable
# creation 
num=(10,20,30)






num=(10,20,30)
print(type(num))
print(num)
print(num[0])
l=[1,2,3]
a=tuple(l)
print(type(a))

"""
"""l=(1,2,3)
l[2]=5
print(l)"""
"""t=(1,2,3)
a,b,c=t
print(a,b,c)"""

"""t=(10,20,[30,40])
(t[2].append(50))
print(t)
a=(1,2,3)
b=(4,6,7)
print(a+b)

t=10,20
print(t*3)
t=(1,2,3,4,5)
for i in t:
    print(i)
    t=(1,2,34,56,1)
print(len(t))
print(t.count(1))
print(t.index(1))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))
"""


student=(101,"John",[75,80,85])

while True:
    print("====student marks manager======")
    print("1.Display student info")
    print("2.Add New marks")
    print("3.Updte Mark")
    print(("4.Total and Avg"))
    print("5.Exit")
    choice=int(input("enter your choice"))
    if choice==1:
        print("Student id",student[0])
        print("Student name",student[1])
        print("Student marks",student[2])
    elif choice==2:
        mark=int(input("enter new mark"))
        student[2].append(mark)
        print("updated marks",student[2])
    elif choice==3:
        print("Current marks",student[2])
        index=int(input(" Enter mark inedx "))
        new_mark=int(input("enter new marks"))
        if 0<=index<len(student[2]):
            student[2][index]=new_mark
            print("marks updated",mark)
        else:
            print("invalid index")
    elif choice==4:
        total=sum(student[2])
        avg=total/len(student[2])
        print("total marks ",total)
        print("avg marks",avg)
    else:
        print("Thank You ")
        break

        

