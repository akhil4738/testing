"""
> multiples tasks at a time 
> multi threading a :
> threading 
from threading import Thread
class Hai(Thread):
    def run(self):
        for i in range(100):
            print("hai")
class Hello(Thread):
    def run(self):
        for i in range(100):
            print("hello")
obj1=Hai()
obj2=Hello()
obj1.start()
obj2.start()
# new State t1=Hello()
# t1.start()
# running 
# wait/block 
from threading import Thread
import time
class MyThread(Thread):
    def run(self):
        print("hello")
        time.sleep(10)
        print("hello again")

t=MyThread()
t.start()
"""

"""
from threading import * 
class HelloThread(Thread):
    def run(self):
        for i in range(5):
            print("hello")

t=HelloThread()
t.start()
t.join()
print("Main Thread Completed ")
from threading import Thread
class Hai(Thread):
    def run(self):
        for i in range(100):
            print("hai")
class Hello(Thread):
    def run(self):
        for i in range(100):
            print("hello")
obj1=Hai()
obj2=Hello()

obj1.start()
obj1.join()

obj2.start()
obj2.join()
"""
