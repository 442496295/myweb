from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor
import time

def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

def pp(n):
    print(n)

if __name__ == '__main__':
    with ThreadPoolExecutor(4) as executor:
    # with ProcessPoolExecutor(4) as executor:
        tasks = [executor.submit(pp, num) for num in range(10000)]
        start_time = time.time()
        for future in as_completed(tasks):
            data = future.result()
            print(data)
    print(time.time() - start_time)
