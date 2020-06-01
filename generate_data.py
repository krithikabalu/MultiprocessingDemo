from random import randint, uniform

import pandas


def generate_data():
    regions = ['India', 'US', 'UK', 'Australia', 'Canada', 'Singapore', 'Sweden', 'Brazil', 'Russia', 'SriLanka']
    df = pandas.DataFrame()
    for i in range(1, 100000):
        new_df = pandas.DataFrame(
            data=[
                [i, regions[randint(0, len(regions) - 1)], round(uniform(0, 1), 2),
                 round(uniform(100000, 1000000), 2)]
            ],
            columns=['id', 'region', 'profit', 'cost'])
        df = pandas.concat([df, new_df])
    df.to_csv('main.csv')


generate_data()
