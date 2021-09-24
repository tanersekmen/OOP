import random
from app import df
# randomly selected horse id and other things.
random_winner = random.randint(1, len(df))
# it returns winner horse with all information in dataframe
print(df.loc[random_winner])


