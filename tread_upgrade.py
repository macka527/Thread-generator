from tqdm import tqdm


def threads_func(threads, n):
    """
    threads_func(threads, n)
    Принимает\n
    threads - список объектов потоков\n
    n - посколько потоков запускать за раз
    """
    def func_chunks_generators(threads, n):
        "Создает список со списками по "
        for i in range(0, len(threads), n):
            yield threads[i : i + n]

    def start_join(threads):
        for x in threads:
            x.start()    
        for x in threads:
            x.join()

    threads_list_list = list(
        func_chunks_generators(threads, n) # n - потоков
    )

    for threads in tqdm(threads_list_list):
        start_join(threads)