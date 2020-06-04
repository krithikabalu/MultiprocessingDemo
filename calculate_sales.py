import uuid

import pandas


def calculate_sales(region):
    df = pandas.read_csv('main.csv')
    df['sales'] = (df['cost'] + df['profit'] * df['cost']).apply(round)
    df['profitable'] = df.apply(
        lambda x: "Yes" if x["sales"] > x["cost"] else "No", axis=1)
    df['profit'] = df['sales'] - df['cost']
    df['profit_percent'] = df['profit'] * 100
    df['profit_percent'] = df['profit_percent'].astype(int)
    df = df[df['profitable'] == 'Yes']
    region_sales = df.groupby(by=['region']).agg({'sales': 'sum'}).rename({'sales': 'total_sales'})
    region_cost = df.groupby(by=['region']).agg({'cost': 'sum'}).rename({'cost': 'total_cost'})
    region_profit = df.groupby(by=['region']).agg({'profit': 'sum'}).rename({'profit': 'total_profit'})
    region_avg_sales = df.groupby(by=['region']).agg({'sales': 'mean'}).rename({'sales': 'avg_sales'})
    region_avg_cost = df.groupby(by=['region']).agg({'cost': 'mean'}).rename({'cost': 'avg_cost'})
    region_avg_profit = df.groupby(by=['region']).agg({'profit': 'mean'}).rename({'profit': 'avg_profit'})
    df[df['region'] == region].to_csv('s3://process-data1/{}.csv'.format(uuid.uuid4()))
