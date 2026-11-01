import pandas as pd 
car_evaluation = {
    'buying':   ['vhigh', 'high',  'med',   'low',   'vhigh', 'low',   'med',   'high',  'low',   'low',   'vhigh', 'med'],
    'maint':    ['vhigh', 'high',  'med',   'low',   'vhigh', 'low',   'med',   'high',  'low',   'low',   'vhigh', 'med'],
    'doors':    ['2',     '3',     '4',     '5more', '2',     '3',     '4',     '5more', '2',     '3',     '4',     '5more'],
    'persons':  ['2',     '4',     'more',  '2',     '4',     'more',  '2',     '4',     'more',  '2',     '4',     'more'],
    'lug_boot': ['small', 'med',   'big',   'small', 'med',   'big',   'small', 'med',   'big',   'small', 'med',   'big'],
    'safety':   ['low',   'med',   'high',  'low',   'med',   'high',  'low',   'med',   'high',  'low',   'med',   'high'],
    'class':    ['unacc', 'acc',   'good',  'vgood', 'unacc', 'acc',   'good',  'vgood', 'unacc', 'acc',   'good',  'vgood']
    }
df = pd.DataFrame(car_evaluation)
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.head(3))
print(df.tail)
