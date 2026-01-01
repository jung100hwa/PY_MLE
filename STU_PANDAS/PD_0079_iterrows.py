import pandas as pd

df = pd.DataFrame(
    {'price': [100, 200, 300],
     'weight': [20.3, 15.1, 25.9]})


for idx, row in df.iterrows():
    print("** index name:", idx)
    print(row)
    
print("=" * 50)

for idx, row in df.iterrows():
    for item in row:
        print(item, end=' ')
    print('')
    
print("=" * 50)

for idx, row in df.iterrows():
    print(row[0], row[1])
 
    
print("=" * 50)


    