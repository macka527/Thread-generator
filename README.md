
# Способ запуска

```python
from threading import Thread
from tread_upgrade import threads_func

threads = []
for item in items: 
    proc = Thread(target=func, args=[items,])
    threads.append(proc)

threads_func(threads, 20)
```
