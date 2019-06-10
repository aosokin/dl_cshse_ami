import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def prepare_data():
    le = LabelEncoder()
    data = pd.read_csv('letter.data', sep='\t', header=None)
    data.pop(134)
    train, test, val = data[data[5] < 8], data[data[5] == 9], data[data[5] == 8]

    y = []
    for row in train.iterrows():
        y.append(row[1][1])
    le = LabelEncoder().fit(y)

    gb, train_x, train_y = train.groupby(3), [], []
    for group in gb.groups.keys():
        chunk_x, chunk_y  = [], []
        for row in gb.get_group(group).iterrows():
            sample = np.zeros((1, 32, 32))
            sample[0, 8:24, 12:20] = np.array(row[1][6:]).reshape((1, 16, 8))
            chunk_x.append(sample), chunk_y.append(row[1][1])
        train_x.append(np.array(chunk_x)), train_y.append(le.transform(np.array(chunk_y)))

    gb, test_x, test_y = test.groupby(3), [], []
    for group in gb.groups.keys():
        chunk_x, chunk_y  = [], []
        for row in gb.get_group(group).iterrows():
            sample = np.zeros((1, 32, 32))
            sample[0, 8:24, 12:20] = np.array(row[1][6:]).reshape((1, 16, 8))
            chunk_x.append(sample), chunk_y.append(row[1][1])
        test_x.append(np.array(chunk_x)), test_y.append(le.transform(np.array(chunk_y)))
    
    gb, val_x, val_y = val.groupby(3), [], []
    for group in gb.groups.keys():
        chunk_x, chunk_y  = [], []
        for row in gb.get_group(group).iterrows():
            sample = np.zeros((1, 32, 32))
            sample[0, 8:24, 12:20] = np.array(row[1][6:]).reshape((1, 16, 8))
            chunk_x.append(sample), chunk_y.append(row[1][1])
        val_x.append(np.array(chunk_x)), val_y.append(le.transform(np.array(chunk_y)))

    return train_x, train_y, test_x, test_y, val_x, val_y, le