import pandas as pd

df = pd.read_csv('production.csv')

new_rows = {
    'Firm1': [150, 160, 170], 
    'Firm2': [180, 190, 200], 
    'Firm3': [210, 220, 230]
}

new_data = pd.DataFrame(new_rows)
df = pd.concat([df, new_data], ignore_index=True)

df.to_csv('all.csv', index=False)
print("Дані збережені у файл all.csv")
