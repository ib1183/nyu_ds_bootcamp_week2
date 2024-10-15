import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df_subset = df[df.index % 20 == 0].filter(items = ['Manufacturer', 'Model', 'Type'])

df['Max.Price'].fillna(df['Max.Price'].mean())
df['Min.Price'].fillna(df['Min.Price'].mean())

df_int = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
df_over_hundred = df_int[df_int.sum(axis = 1) > 100]

if __name__ == '__main__':
    print(df_subset)
    print(df_over_hundred)
