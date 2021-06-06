import threading
import time
import random
queue = []
full = threading.Semaphore(0)
empty = threading.Semaphore(1)

def producer():
	nums = range(3)
	global queue
	while True:
		num = random.choice(nums)
		empty.acquire()
		queue.append(num)
		print("Produced", num, queue)
		full.release()
		time.sleep(random.randrange(0, 3))


def consumer():
	global queue
	while True:
		full.acquire()
		num = queue.pop(0)
		print("Consumed", num, queue)
		empty.release()
		time.sleep(random.randrange(0, 3))

producerThread = threading.Thread(target=producer)
consumerThread = threading.Thread(target=consumer)

producerThread.start()
consumerThread.start()