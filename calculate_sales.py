import uuid


def save(df):
    df.to_csv('output/{}.csv'.format(str(uuid.uuid4())), index=False)


def calculate_sales(df):
    df['sales'] = (df['cost'] + df['profit'] * df['cost']).apply(round)
    df['profitable'] = df.apply(
        lambda x: "Yes" if x["sales"] > x["cost"] else "No", axis=1)
    return df


def calculate_sales_and_save(df):
    save(calculate_sales(df))
