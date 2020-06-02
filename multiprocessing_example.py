import multiprocessing as mlp
from datetime import datetime
import time

import pandas

from calculate_sales import calculate_sales


def process():
    regions = ['India', 'US', 'UK', 'Australia', 'Canada', 'Singapore', 'Sweden', 'Brazil', 'Russia', 'SriLanka']
    df = pandas.read_csv('main.csv')
    start = datetime.now()
    pool = mlp.Pool(mlp.cpu_count())
    for region in regions:
        pool.apply_async(calculate_sales, args=(df[df['region'] == region],))
    pool.close()
    pool.join()
    print('Execution time: {} '.format((datetime.now() - start).microseconds))


# process()

def mp(func, args):
    marker = time.time()
    pool = mlp.Pool(mlp.cpu_count())
    pool.apply_async(func, args=(args,))
    pool.close()
    pool.join()
    return time.time() - marker
