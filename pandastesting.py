import pandas as pd

data={
    "Name":["A","B","C","D"],
    "Marks":[78,85,None,90]
}

df=pd.DataFrame(data)

print(df)
print(df.isnull())
print(df["Marks"].mean())