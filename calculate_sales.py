import uuid


def calculate_sales(df):
    df['sales'] = (df['cost'] + df['profit'] * df['cost']).apply(round)
    df['profitable'] = df.apply(
        lambda x: "Yes" if x["sales"] > x["cost"] else "No", axis=1)
    df.to_csv('output/{}.csv'.format(str(uuid.uuid4())), index=False)
