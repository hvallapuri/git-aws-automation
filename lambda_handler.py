import pandas as pd


def handler(event, context):
    data = pd.DataFrame({'column1': [10, 15], 'column2': [8, 7]})
    print(data)

