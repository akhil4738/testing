""""
> A set is collection of unordered , mutable collection of unique elements
using { }


"""
students={"daniel", "ram ","rojan"}
while True:
    print("===== Student Manager======")
    print("1.Add Student")
    print("2.Display students")
    print("3.update student")
    print("4.delete student")
    print("5.Exit")
    action=int(input("enter a value from 1-4"))
    if action==1:
        name=input("enter student name ")
        students.add(name)
        print("Student is added ")
    elif action==2:
        for i in students:
            print(i)
    elif action==3:
        old_name=input("enter old name ")
        new_name=input("enter new name ")
        if old_name in students:
            students.remove(old_name)
            students.add(new_name)
            print("Student updated")
        else:
            print("old name is not present ")
    elif action==4:
        name=input("enter a name to remove")
        if name in students:
            students.remove(name)
            print("student removed ")
        else:
            print("name is not present in students to remove")
    else:
        print("Thank you ")
        break



        
