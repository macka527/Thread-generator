

from threading import Thread
threads = []
for item in items: 
    proc = Thread(target=func, args=[items,])
    threads.append(proc)

threads_func(threads, 20)
