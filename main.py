import multiprocessing as mlp
import time
from concurrent.futures.thread import ThreadPoolExecutor

import matplotlib.pyplot as plt
import pandas

from calculate_sales import calculate_sales


def visualize(mt_results, mp_results, title):
    plt.plot(range(len(mt_results)), mt_results, color='green', marker='o')
    plt.plot(range(len(mp_results)), mp_results, color='red', marker='*')
    plt.ylabel("Time")
    plt.xlabel("jobs")
    plt.title(title)
    plt.legend(["Thread", "Process"])
    plt.show()


def measure(func):
    marker = time.time()
    func(0)
    return time.time() - marker


def multiprocess(func, arguments):
    pool = mlp.Pool(mlp.cpu_count())
    [pool.apply(func, args=(arg,)) for arg in arguments]
    pool.close()
    pool.join()


def multithread(func, arguments):
    executor = ThreadPoolExecutor(10 * mlp.cpu_count())
    [executor.submit(func, arg) for arg in arguments]
    executor.shutdown(wait=True)


size = 3
regions = ['India', 'US', 'UK', 'Australia', 'Canada', 'Singapore', 'Sweden', 'Brazil']

df = pandas.read_csv('main.csv')
print(df.head())
# [measure(lambda _: multiprocess(calculate_sales, arguments=(df, regions*j))) for j in range(1,size+1)]
# [measure(lambda _: multithread(calculate_sales, arguments=(df, regions*i))) for i in range(1,size+1)]
visualize([measure(lambda _: multithread(calculate_sales, arguments=regions * i)) for i in range(1, size + 1)],
          [measure(lambda _: multiprocess(calculate_sales, arguments=regions * j)) for j in range(1, size + 1)],
          'multithreading vs multiprocessing - local io')

# aws configure
# aws sts get-session-token
