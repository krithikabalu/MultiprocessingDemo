import multiprocessing as mlp
import time
import urllib.request
import uuid
from concurrent.futures.thread import ThreadPoolExecutor

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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


def count(num):
    for var in range(100000):
        num += var


def save_csv(func, args):
    df = pd.read_csv('main.csv')
    dfs = [df[df['region'] == region] for region in args]
    return func(lambda x: x.to_csv(f"output/{uuid.uuid4()}.csv"), dfs)


def connect_url(in_str):
    with urllib.request.urlopen(f"https://www.google.com?q={in_str}") as f:
        pass


def mp(func, args):
    pool = mlp.Pool(mlp.cpu_count())
    [pool.apply_async(func, args=(arg,)) for arg in args]
    pool.close()
    pool.join()


def mt(func, args):
    executor = ThreadPoolExecutor(10 * mlp.cpu_count())
    [executor.submit(func, arg) for arg in args]
    executor.shutdown(wait=True)


size = 10

visualize([measure(lambda _: mt(count, np.ones(i + 1))) for i in range(size)],
          [measure(lambda _: mp(count, np.ones(i + 1))) for i in range(size)],
          'multithreading vs multiprocessing - cpu')

visualize([measure(lambda _: mt(connect_url, np.ones(i + 1))) for i in range(size)],
          [measure(lambda _: mp(connect_url, np.ones(i + 1))) for i in range(size)],
          'multithreading vs multiprocessing - io')

# regions = ['India', 'US', 'UK', 'Australia', 'Canada', 'Singapore', 'Sweden', 'Brazil', 'Russia', 'SriLanka']
# visualize([measure(lambda _: save_csv(mt, regions * i)) for i in range(size)],
#           [measure(lambda _: save_csv(mp, regions * i)) for i in range(size)],
#           'multithreading vs multiprocessing - local io')
