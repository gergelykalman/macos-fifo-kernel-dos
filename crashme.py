#!/usr/bin/python3

import os
import queue
import time

n = 4
size = 128*1024*1024

buf = bytearray(os.urandom(size))
for x in range(n):
	q = queue.Queue()
	if os.fork() == 0:
		while True:
			new_data = buf.copy()
			q.put((new_data))

time.sleep(10)

