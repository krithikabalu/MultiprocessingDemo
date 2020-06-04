import multiprocessing as mlp
from concurrent.futures.thread import ThreadPoolExecutor


def mp(func, args):
    pool = mlp.Pool(mlp.cpu_count())
    res = [pool.apply_async(func, args=(arg,)) for arg in args]
    pool.close()
    pool.join()
    return [r.get() for r in res]


def mt(func, args):
    executor = ThreadPoolExecutor(10 * mlp.cpu_count())
    [executor.submit(func, arg) for arg in args]
    executor.shutdown(wait=True)
