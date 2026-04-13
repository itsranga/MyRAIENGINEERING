import seaborn as sns
import pandas as pd

data=sns.load_dataset("tips")

sns.boxplot(x="day",y="total_bill",data=data)