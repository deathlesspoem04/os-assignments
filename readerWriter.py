'''
@Assignment: Reader Writer Problem
@Student Name: Vishesh Sinha
@Roll: 11948 
'''

import threading as thread
import random

global data
data = 0
lock = thread.Lock()

def Reader():
    global data
    print('Reading!')
    lock.acquire()      
    print(f'Shared Data:{data}')
    lock.release()
    print()

def Writer():
    global data
    print('Writing!')
    lock.acquire()     
    data += 1              
    print(f'Written:{data}')
    lock.release()      
    print()

if __name__ == '__main__':
    for i in range(0, 20):
        randomNumber = random.randint(0, 10)   #Generate a Random number between 0 to 100
        if(randomNumber > 5):
            thread1 = thread.Thread(target = Reader)
            thread1.start()
        else:
            thread2 = thread.Thread(target = Writer)
            thread2.start()

thread1.join()
thread2.join()