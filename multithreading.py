#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import queue
import threading
import time

exitFlag = 0
# threadLock = threading.Lock()
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadId = 1


class MyThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        # threadLock.acquire()
        TimeFunc(self, self.counter, 3)
        # threadLock.release()
        print("Exiting " + self.name)


def TimeFunc(thread, delay):
    # while counter:
    # if exitFlag:
    #     thread.exit()
    # time.sleep(delay)
    # counter -= 1
    # print("%s: %s" % (thread, time.ctime(time.time())))
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = delay.get()
            queueLock.release()
            print("%s processing %s " % (thread, data))


threadList = ["Thread1", "Thread2", "Thread3"]
nameList = ["One", "Two", "Three"]

for i in threadList:
    thread = MyThread(threadId, i, workQueue)
    thread.start()
    threads.append(thread)
    threadId += 1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1

# threads = []
# thread1 = MyThread(1, "test1", 5)
# thread2 = MyThread(2, "test2", 5)
# thread3 = MyThread(3, "test3", 5)
#
# thread1.start()
# thread2.start()
# thread3.start()
#
# threads.append(thread1)
# threads.append(thread2)
# threads.append(thread3)
#
for thread in threads:
    thread.join()
