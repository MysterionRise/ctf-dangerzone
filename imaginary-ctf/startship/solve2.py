import pandas as pd
from io import StringIO
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

dataset_csv = """x,y,velocity,rotation,price,rizz,anger,patience,aura,classification
35,58,87,62,77,46,51,131,91,friendly
74,111,58,19,-25,39,50,50,111,enemy
47,79,68,4,65,79,114,66,57,friendly
38,83,87,63,107,60,65,118,112,friendly
57,53,39,-12,-29,20,87,89,127,enemy
56,119,44,23,70,62,76,97,94,friendly
78,76,59,3,8,84,75,72,86,enemy
35,121,40,57,96,67,59,132,64,friendly
1,102,43,44,111,69,54,129,66,friendly
64,67,23,3,-10,19,40,77,71,enemy
73,49,14,-23,-2,32,56,86,106,enemy
7,74,63,3,87,47,66,70,109,friendly
112,94,62,-28,-6,29,35,104,125,enemy
31,113,85,49,59,55,93,75,97,friendly
47,58,42,22,70,73,93,81,67,friendly
29,95,75,37,102,33,59,72,78,friendly
91,92,16,21,26,87,35,86,121,enemy
112,51,55,15,34,18,72,60,63,enemy
-6,68,64,53,105,74,66,117,90,friendly
70,62,25,18,7,21,35,117,112,enemy
101,67,60,26,-8,46,78,115,99,enemy
73,72,6,-6,-6,69,83,112,103,enemy
91,62,5,3,10,36,82,119,64,enemy
97,115,16,35,5,63,85,105,112,enemy
30,99,46,57,57,84,85,70,59,friendly
53,63,24,-6,30,26,65,74,130,enemy
52,115,56,61,74,48,76,66,44,friendly
12,85,37,35,87,88,87,77,76,friendly
98,101,51,-18,-18,59,68,73,78,enemy
11,63,87,46,63,85,65,122,86,friendly
44,66,89,24,74,44,62,66,94,friendly
92,106,35,-8,-13,50,33,62,66,enemy
33,61,67,6,83,30,49,91,89,friendly
110,54,41,-1,18,30,54,113,70,enemy
109,66,71,4,20,46,29,67,77,enemy
64,66,42,58,62,88,108,71,81,friendly
91,64,7,-32,32,69,71,118,119,enemy
18,100,24,18,70,29,75,117,110,friendly
18,63,23,10,69,78,51,82,95,friendly
-1,65,39,59,74,82,69,77,61,friendly
71,79,53,29,4,56,40,117,98,enemy
98,73,43,-25,6,72,50,75,76,enemy
35,58,54,58,122,78,99,89,83,friendly
64,78,47,4,95,78,115,98,78,friendly
107,112,70,-30,10,50,60,67,108,enemy
102,113,70,13,13,86,72,96,121,enemy
63,71,46,30,-17,34,43,76,71,enemy
5,56,22,34,107,29,59,96,102,friendly
118,65,20,-23,-27,18,86,76,88,enemy
3,108,32,7,64,88,115,83,102,friendly
76,87,71,10,34,24,30,76,126,enemy
70,77,46,-14,30,52,95,68,120,enemy
77,62,53,-28,33,49,95,74,108,enemy
53,78,59,58,97,77,73,79,100,friendly
19,60,87,14,108,90,67,118,110,friendly
96,113,38,-31,-7,68,77,119,120,enemy
108,48,3,12,-28,74,31,64,72,enemy
9,106,28,4,123,39,78,106,113,friendly
36,125,42,1,91,25,93,109,47,friendly
-4,113,67,46,56,32,102,79,54,friendly

"""
targets_csv = """100,86,67,79,67,44,18,92,6
95,68,102,41,47,43,62,79,-25"""

df = pd.read_csv(StringIO(dataset_csv))
targets_df = pd.read_csv(StringIO(targets_csv), header=None)

X, y = df.iloc[:, :-1].values, df.iloc[:, -1].values


def predict_with_new_entry(new_entry):
    # Add the new entry to the dataset
    new_X = np.vstack([X, new_entry])
    new_y = np.append(y, 'friendly')
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(new_X, new_y)
    predictions = model.predict(targets_df.values)
    return predictions


X, y = df.iloc[:, :-1].values, df.iloc[:, -1].values

friendly_data = df[df['classification'] == 'friendly'].iloc[:, :-1].values
enemy_data = df[df['classification'] == 'enemy'].iloc[:, :-1].values


def predict_with_new_entry(new_entry):
    new_X = np.vstack([X, new_entry])
    new_y = np.append(y, 'friendly')
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(new_X, new_y)
    predictions = model.predict(targets_df.values)
    return predictions


best_entry = None
best_score = -1

friendly_min = friendly_data.min(axis=0)
friendly_max = friendly_data.max(axis=0)

for _ in range(100000):
    new_entry = np.random.uniform(friendly_min, friendly_max)
    predictions = predict_with_new_entry(new_entry)

    score = sum(predictions == 'friendly')

    if score > best_score:
        best_score = score
        best_entry = new_entry

    if score == len(targets_df):
        break

print(f'Best new entry: {best_entry}')
print(f'Predictions with best new entry: {predict_with_new_entry(best_entry)}')

new_row = pd.DataFrame([list(best_entry) + ['friendly']], columns=df.columns)
new_df = pd.concat([df, new_row], ignore_index=True)

new_df.to_csv('updated_dataset.csv', index=False)