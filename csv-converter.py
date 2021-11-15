from spotify_review_data import reviews
import pandas as pd
import numpy as np
import json

df = pd.DataFrame(np.array(reviews),columns=['review'])
df2 = df.join(pd.DataFrame(df.pop('review').tolist()))
df2.head()
df2.to_csv('/Users/ninamutty/Projects/hci-2/hci-project/sportify-reviews.csv')