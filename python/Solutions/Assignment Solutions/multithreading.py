from threading import Thread, current_thread

class Display():

    def evenNum(self):
        print(current_thread().getName())
        for i in range(1, 11):
            if i % 2 == 0:
                print(i)

    def oddNum(self):
        print(current_thread().getName())
        for i in range(1, 11):
            if i % 2 != 0:
                print(i)

    def printNum(self):
        print(current_thread().getName())
        for i in range(1, 101):
            print(i)


d = Display()
d.printNum()
t1 = Thread(target=d.evenNum)
t1.start()
t2 = Thread(target=d.oddNum)
t2.start()