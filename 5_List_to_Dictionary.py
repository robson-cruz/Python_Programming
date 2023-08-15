import pandas as pd


labels = ['Country', 'City', 'Currency']
sublist = [['England', 'London', 'GBP'], ['France', 'Paris', 'EUR'], ['Germany', 'Berlin', 'EUR']]


def list_to_dict(x, y):
    new_dict = {key: value for key, value in zip(x, y)}
    return new_dict


list_of_dicts = [list_to_dict(labels, items) for items in sublist]
print(list_of_dicts)

df = pd.DataFrame(list_of_dicts)
print(df)