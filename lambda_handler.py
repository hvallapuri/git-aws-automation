import pandas as pd


def handler(event, context):
    data = {'column1': [10.8, 15.9], 'column2': [8, 7]}
    df = pd.DataFrame(data)
    print(df)
    print("Processing completed")
