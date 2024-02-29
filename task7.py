# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.
from random import randint
import asyncio
from multiprocessing import Process, Queue
import threading
import time


def calculate_sum_thread(arr, result):
    sum = 0
    for i in arr:
        sum += i
    result.append(sum)


def thread_sum_arr(arr):
    result = []
    threads = []
    start_time = time.time()

    chunk_size = len(arr) // 1_000
    for i in range(0, len(arr), chunk_size):
        chunk = arr[i:i + chunk_size]
        thread = threading.Thread(target=calculate_sum_thread, args=(chunk, result))
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()

    total_sum = sum(result)
    print(f'Время выполнения многопоточного решения: {time.time() - start_time} сек')
    print(f'Сумма элементов массива (многопоточность): {total_sum}')


def calculate_sum_multiproces(arr, result):
    sum = 0
    for i in arr:
        sum += i
    result.put(sum)

def multiprocess_sum_arr(arr):
    result = Queue()
    processes = []
    start_time = time.time()

    chunk_size = len(arr) // 1_000
    for i in range(0, len(arr), chunk_size):
        chunk = arr[i:i + chunk_size]
        process = Process(target=calculate_sum_multiproces, args=(chunk, result))
        processes.append(process)
        process.start()

    for p in processes:
        p.join()

    total_sum = 0
    while not result.empty():
        total_sum += result.get()

    print(f'Время выполнения многопроцессорного решения: {time.time() - start_time} сек')
    print(f'Сумма элементов массива (многопроцессорность): {total_sum}')


async def calculate_sum_async(arr, result):
    sum = 0
    for i in arr:
        sum += i
    result.append(sum)

async def async_sum_arr(arr):
    result = []
    start_time = time.time()

    chunk_size = len(arr) // 1_000
    tasks = []
    for i in range(0, len(arr), chunk_size):
        chunk = arr[i:i + chunk_size]
        task = asyncio.ensure_future(calculate_sum_async(chunk, result))
        tasks.append(task)

    await asyncio.gather(*tasks)

    total_sum = sum(result)
    print(f'Время выполнения асинхронного решения: {time.time() - start_time} сек')
    print(f'Сумма элементов массива (асинхронность): {total_sum}')


if __name__ == '__main__':
    arr = [randint(1, 100) for _ in range(1_000)]
    thread_sum_arr(arr)
    multiprocess_sum_arr(arr)
    asyncio.run(async_sum_arr(arr))


