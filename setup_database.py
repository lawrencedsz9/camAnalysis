import sqlite3


conn = sqlite3.connect('setup_database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS recordings (
    id INTEGER PRIMARY KEY,
    name TEXT,
    timestamp TEXT
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS in_records (
    id INTEGER PRIMARY KEY,
    name TEXT,
    timestamp TEXT
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS out_records (
    id INTEGER PRIMARY KEY,
    name TEXT,
    timestamp TEXT
)
''')


cursor.execute('''
INSERT INTO recordings (name, timestamp)
VALUES ('Recording1', '2024-07-16 10:00:00')
''')

cursor.execute('''
INSERT INTO recordings (name, timestamp)
VALUES ('Recording2', '2024-07-16 10:05:00')
''')

cursor.execute('''
INSERT INTO in_records (name, timestamp)
VALUES ('InRecord1', '2024-07-16 10:10:00')
''')

cursor.execute('''
INSERT INTO in_records (name, timestamp)
VALUES ('InRecord2', '2024-07-16 10:15:00')
''')


cursor.execute('''
INSERT INTO out_records (name, timestamp)
VALUES ('OutRecord1', '2024-07-16 10:20:00')
''')

cursor.execute('''
INSERT INTO out_records (name, timestamp)
VALUES ('OutRecord2', '2024-07-16 10:25:00')
''')


conn.commit()
conn.close()

print("Database, tables created, and data inserted successfully.")
