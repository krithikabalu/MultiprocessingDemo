import time
import matplotlib.pyplot as plt
import urllib.request
import numpy as np
import pandas as pd
from calculate_sales import calculate_sales_and_save, calculate_sales, save
from utils import mt, mp


def visualize(mt_results, mp_results, title):
    plt.plot(range(len(mt_results)), mt_results, color='green', marker='o')
    if mp_results:
        plt.plot(range(len(mp_results)), mp_results, color='red', marker='*')
    plt.ylabel("Time")
    plt.xlabel("jobs")
    plt.title(title)
    if mp_results:
        plt.legend(["Thread", "Process"])
    plt.show()


def measure(func):
    marker = time.time()
    func(0)
    return time.time() - marker


def count(num):
    for var in range(100000):
        num += var


def connect_url(in_str):
    with urllib.request.urlopen(f"https://www.google.com?q={in_str}") as f:
        pass


df = pd.read_csv('main.csv')
input_regions = ['India', 'US', 'UK', 'Australia', 'Canada', 'Singapore', 'Sweden', 'Brazil', 'Russia', 'SriLanka'] * 2


def calculate_sales_for_regions(region):
    calculate_sales_and_save(df[df['region'] == region])


def calculate_sales_curry(region):
    return calculate_sales(df[df['region'] == region])


def calculate_sales_for_regions_optimized(regions):
    region_results = mp(calculate_sales_curry, regions)
    mt(save, region_results)


size = 20

visualize([measure(lambda _: mt(count, np.ones(i + 1))) for i in range(size)],
          [measure(lambda _: mp(count, np.ones(i + 1))) for i in range(size)],
          'multithreading vs multiprocessing - cpu')

visualize([measure(lambda _: mt(connect_url, np.ones(i + 1))) for i in range(size)],
          [measure(lambda _: mp(connect_url, np.ones(i + 1))) for i in range(size)],
          'multithreading vs multiprocessing - io')

visualize([measure(lambda _: mt(calculate_sales_for_regions, input_regions[0:i + 1])) for i in range(size)],
          [measure(lambda _: mp(calculate_sales_for_regions, input_regions[0:i + 1])) for i in range(size)],
          'multithreading vs multiprocessing - io & CPU')

results = [measure(lambda _: calculate_sales_for_regions_optimized(input_regions[0:i + 1])) for i in range(size)]
visualize(results, None, 'optimized')
