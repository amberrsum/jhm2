import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NewYork', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("\nAccess the 'Name' column:")
print(df['Name'])

print("\nAccess the second row using iloc:")
print(df.iloc[1])

df['Salary']=[70000, 80000, 75000]
print("\nDaraFrame after adding a new column 'Salary': ")
print(df)

filtered_df = df[df['age']]