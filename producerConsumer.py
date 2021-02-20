'''
@Assignment: Producer Consumer Problem with shared memory model
@Student Name: Vishesh Sinha
@Roll: 11948 
'''

from threading import Thread, Condition
import time
import random


queue = []
MAX_NUM = 10
condition = Condition() # Condition object allows one or more threads to wait until notified by another thread. 

class ProducerThread(Thread):
    def run(self):
        nums = range(5)

        global queue
        
        while True:
            
            condition.acquire()
            if len(queue) == MAX_NUM:   # Producer should not put data in the queue if the queue is full.
                print("Queue is full, producer is waiting")
                condition.wait()
                print("Space in queue, Consumer notified the producer")
            num = random.choice(nums)
            queue.append(num)
            print("Produced", num)
            condition.notify()
            condition.release()
            time.sleep(random.random())

class ConsumerThread(Thread):
    def run(self):
        global queue

        while True:
            
            condition.acquire()
            if not queue:
                print("Nothing in Queue")
                condition.wait()
                print("Producer added something to queue and notified the consumer")
            num = queue.pop(0)
            print("Consumed", num)
            condition.notify()
            condition.release()
            time.sleep(random.random())

# Starts the Process

ProducerThread().start()
ConsumerThread().start()

