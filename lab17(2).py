import pandas as pd

months = ('Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень')

production = []
for month in months:
    quantity = int(input(f"Введіть кількість випущених бетонних плит для {month}: "))
    production.append(quantity)

series = pd.Series(production, index=months)

series.to_json('beton.json', force_ascii=False, indent=4)
print("Дані збережені у файл beton.json")
