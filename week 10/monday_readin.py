# reading in data first
import sqlite3

# connection and cursor objects

# connect function to open connection
con = sqlite3.connect('letters.db')
# cursor method to make c object
c = con.cursor()

# lets look at content

## execute method

results = c.execute("SELECT * FROM letter;")
## you can iterate, but that's messy
# print(results)
# for each in results:
#     print(each)

data = results.fetchall()
print(type(data))

print(len(data))
print(data[:5])
print(results.description)
headers = [row[0] for row in results.description]
print(headers)

for r in data:
    print(r)

