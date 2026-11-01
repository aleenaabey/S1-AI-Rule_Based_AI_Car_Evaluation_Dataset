import pandas as pd

# 1. Create a mini table of 5 cars
car_table = pd.DataFrame({
    'buying': ['vhigh', 'low', 'med', 'vhigh', 'low'],
    'maint': ['high', 'low', 'med', 'vhigh', 'low'],
    'safety': ['low', 'high', 'med', 'low', 'high'],
    'verdict': ['unacc', 'vgood', 'acc', 'unacc', 'good']
})
print(car_table)
