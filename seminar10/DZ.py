# %%
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()


# %%
check = list(data['whoAmI'].unique())
for i in check:
    data.loc[data['whoAmI'] == i, i] = 1
    data.loc[data['whoAmI'] != i, i] = 0
data.head()