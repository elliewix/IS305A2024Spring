import sqlite3

conn = sqlite3.connect('newdata.sqlite')

c = conn.cursor()
# same as before, but we'll use SQL to make
# a table

# use create table to make table
# add if not exists as needed
c.execute('CREATE TABLE IF NOT EXISTS letters (letter text, count integer);')


sentence = "here's some stuff cats make sounds. they are loud"

from collections import Counter
counted_letters = Counter(sentence)
total = len(sentence)

data = [[k, v, round(v/total,2)] for k, v in counted_letters.items()]
# print(data)
headers = ["letter", "count", "proportion"]

c.execute("CREATE TABLE IF NOT EXISTS char_counts " +
          "(letter text, count integer, proportion real);")

c.executemany("INSERT INTO char_counts VALUES (?, ?, ?)", data)

conn.commit()