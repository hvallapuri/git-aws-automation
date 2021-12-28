import pandas as pd


def handler(event, context):
    data = {'column1': [10, 15], 'column2': [8, 7]}
    df = pd.DataFrame(data)
    print(df)
