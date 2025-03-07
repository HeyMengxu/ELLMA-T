import sqlite3

conn = sqlite3.connect('D:\sqliteDB\demo.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM userSign WHERE vrcode = ?', ('VR-A001',))
rows = cursor.fetchall()
for row in rows:
    print(row)

if(len(rows) == 0):
    cursor.execute('INSERT INTO userSign (vrcode, username) VALUES (?, ?)', ('VR-A001', 'available'))

if(len(rows) > 0):
    cursor.execute('''
UPDATE userSign
SET username = ?
WHERE vrcode = ?
''', ('available', 'VR-A001'))
    
# 提交更改
conn.commit()

cursor.execute('SELECT * FROM userSign WHERE vrcode = ?', ('VR-A001',))
rows = cursor.fetchall()
for row in rows:
    print(row)

# 关闭连接
cursor.close()
conn.close()






