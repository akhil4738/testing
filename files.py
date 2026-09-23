""".txt 


hello iam python_user 


.csv 

id , name 
1, akhil
2, nikhil
...

.json 
{
name:"akhil"
age=25
}

.py
--------------------------
image
.jpg 
.jpeg 
.png 
.webp
.gif





try:

    fp=open("file1.txt","w")
    data=fp.read()
    print(data)
    fp.close()
except Exception as e:
    print(e)

    



if fp:
    print("file opened ")



file=open("data.txt","w")
file.write("welcome to Python Files \n")
file.write("welcome to Python Files \n")
file.write("welcome to Python Files \n")
file.write("welcome to Python Files \n")
file.close
print("data is written into file ")
file=open("data.txt","r")
data=file.read()
print(data)
"""
"""name=input("enter your name")
file=open("data.txt","w")
file.write("my name is "+name)

file.close()
print("name is written into file")"""

"""
fp=open("file.txt","a")
fp.write("\n Im a line written using append mode\n")
fp.close()
print("new line aded")
num=int(input("enter a number"))
fp=open("count.txt","a")
for i in range(1, num+1):
    fp.write(str(i)+"\n")
fp.close()
print("numbers inserted ")


seach=input("enter a word to search ")
fp=open("count.txt","r")
data=fp.read()
fp.close
if seach in data:
    print("number found")
else:
    print("Number Not found")
"""


while True:
    print("Student Notes Manager ")
    print("1.Add Notes ")
    print("2.View Notes ")
    print("3.search Notes ")
    print("4.delete All Notes")
    option=int(input("enter a choice"))
    #adding notes 
    if option==1:
        note=input("enter your notes ")
        fp=open("notes.txt","a")
        fp.write(note+"\n")
        print("Note Saved Successfuly")
    elif option==2:
        data=fp.read()
        print(data)
    elif option==3:
        seach=input("enter a word to search ")
        data=fp.read()
        fp.close
        if seach in data:
            print("number found")
        else:
            print("Number Not found")
    else:
        confirm=input("delete all notes ? (yes /no )")
        if confirm.lower()=="yes":
            fp=open("notes.txt","w")
            fp.write("")
            print("All Notes deleted ")

