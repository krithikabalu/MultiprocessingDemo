from multithreading_example import mt
from multiprocessing_example import mp
from count import count
from visualize import visualize
import numpy as np
import pandas as pd
import uuid

size = 20
visualize([mt(count, np.ones(i + 1)) for i in range(size)],
          [mp(count, np.ones(i + 1)) for i in range(size)],
          'multithreading vs multiprocessing - cpu')


def process(func, args):
    df = pd.read_csv('main.csv')
    dfs = [df[df['region'] == region] for region in args]
    return func(lambda x: x.to_csv(f"output/{uuid.uuid4()}.csv"), dfs)


regions = ['India', 'US', 'UK', 'Australia', 'Canada', 'Singapore', 'Sweden', 'Brazil', 'Russia', 'SriLanka']
visualize([process(mt, regions * i) for i in range(size)],
          [process(mp, regions * i) for i in range(size)],
          'multithreading vs multiprocessing - io')
