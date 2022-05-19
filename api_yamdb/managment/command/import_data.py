import sqlite3

import pandas

connection = sqlite3.connect('db.sqlite3')

df = pandas.read_csv(
    'titles.csv',
    sep=',',
    header=0
)
df.to_sql('reviews_title', connection, if_exists='append', index=False)

df = pandas.read_csv('users.csv',
                     sep=',',
                     header=0
                     )
df.to_sql('users_user', connection, if_exists='append', index=False)

df = pandas.read_csv(
    'review.csv',
    sep=',',
    header=0
)
df.to_sql('reviews_review', connection, if_exists='append', index=False)

df = pandas.read_csv(
    'category.csv',
    sep=',',
    header=0
)
df.to_sql('reviews_category', connection, if_exists='append', index=False)

df = pandas.read_csv(
    'comments.csv',
    sep=',',
    header=0
)
df.to_sql('reviews_comment', connection, if_exists='append', index=False)

df = pandas.read_csv(
    'genre_title.csv',
    sep=',',
    header=0
)
df.to_sql('reviews_genre_title', connection, if_exists='append', index=False)

df = pandas.read_csv(
    'genre.csv',
    sep=',',
    header=0
)
df.to_sql('reviews_genre', connection, if_exists='append', index=False)
