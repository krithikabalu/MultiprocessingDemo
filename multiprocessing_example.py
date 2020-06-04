import multiprocessing as mp
from datetime import datetime

from calculate_sales import calculate_sales


def process():
    regions = ['India', 'US', 'UK', 'Australia', 'Canada', 'Singapore', 'Sweden', 'Brazil', 'Russia', 'SriLanka']
    start = datetime.now()
    pool = mp.Pool(mp.cpu_count())
    for region in regions:
        pool.apply_async(calculate_sales, args=(region,))
    pool.close()
    pool.join()
    print('Execution time: {} '.format((datetime.now() - start).microseconds))


process()
