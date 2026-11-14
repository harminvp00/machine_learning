
import pandas as pd
import matplotlib.pyplot as plt

# reading csv file,
df = pd.read_csv('houses.csv')
# print(df.info())

# converting string data to the numerical classes 0/1, Binary Encoding
df['mainroad'] = df['mainroad'].replace({"yes":1, "no":0})
df['guestroom'] = df['guestroom'].replace({"yes":1, "no":0})
df['basement'] = df['basement'].replace({"yes":1, "no":0})
df['hotwaterheating'] = df['hotwaterheating'].replace({"yes":1, "no":0})
df['airconditioning'] = df['airconditioning'].replace({"yes":1, "no":0})
df['prefarea'] = df['prefarea'].replace({"yes":1, "no":0})

# One hot encoding, represent multi class data in 100, 010, 001 format
df = pd.get_dummies(df, columns=['furnishingstatus'], dtype=int)
df = df.rename(columns={
    "furnishingstatus_furnished":"furnished", 
    "furnishingstatus_semi-furnished": "semi-furnished", 
    "furnishingstatus_unfurnished": "unfurnished" 
    })

plt.plot(df['area'])
plt.ylabel("area")
plt.show()