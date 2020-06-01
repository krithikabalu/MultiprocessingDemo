import multiprocessing as mp
from concurrent.futures.thread import ThreadPoolExecutor
from datetime import datetime

import pandas

from calculate_sales import calculate_sales


def process():
    regions = ['India', 'US', 'UK', 'Australia', 'Canada', 'Singapore', 'Sweden', 'Brazil', 'Russia', 'SriLanka']
    df = pandas.read_csv('main.csv')
    start = datetime.now()
    executor = ThreadPoolExecutor(mp.cpu_count())
    for region in regions:
        executor.submit(calculate_sales, df[df['region'] == region])
    executor.shutdown(wait=True)
    print('Execution time: {} '.format((datetime.now() - start).microseconds))


process()
