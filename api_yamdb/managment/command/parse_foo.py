import sqlite3

import pandas


connection = sqlite3.connect('db.sqlite3')

df = pandas.read_csv('titles.csv', sep=',', header=0)
df.to_sql('titles', connection, if_exists='append')