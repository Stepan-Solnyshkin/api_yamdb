import sqlite3

import pandas

connection = sqlite3.connect('api_yamdb/db.sqlite3')

df = pandas.read_csv(
    'api_yamdb/managment/command/titles.csv',
    sep=',',
    header=0
)
df.to_sql('titles', connection, if_exists='append', index=False)

df = pandas.read_csv(
    'api_yamdb/managment/command/users.csv',
    sep=',',
    header=0
)
df.to_sql('users', connection, if_exists='append', index=False)

df = pandas.read_csv(
    'api_yamdb/managment/command/review.csv',
    sep=',',
    header=0
)
df.to_sql('review', connection, if_exists='append', index=False)

df = pandas.read_csv(
    'api_yamdb/managment/command/category.csv',
    sep=',',
    header=0
)
df.to_sql('category', connection, if_exists='append', index=False)

df = pandas.read_csv(
    'api_yamdb/managment/command/comments.csv',
    sep=',',
    header=0
)
df.to_sql('comments', connection, if_exists='append', index=False)

df = pandas.read_csv(
    'api_yamdb/managment/command/genre_title.csv',
    sep=',',
    header=0
)
df.to_sql('genre_title', connection, if_exists='append', index=False)

df = pandas.read_csv(
    'api_yamdb/managment/command/genre.csv',
    sep=',',
    header=0
)
df.to_sql('genre', connection, if_exists='append', index=False)

df = pandas.read_csv(
    'api_yamdb/managment/command/review.csv',
    sep=',',
    header=0
)
df.to_sql('review', connection, if_exists='append', index=False)
