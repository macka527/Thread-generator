
# Способ запуска

```python
from threading import Thread
from tread_upgrade import threads_func

if __name__ == '__main__':
threads = []
for item in items: 
    proc = Thread(target=func, args=[items,])
    threads.append(proc)

threads_func(threads, 20)
```
