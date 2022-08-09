import sqlite3 as sl
import db_query
import calculation_input as ci

df = ci.Read_csv.read_csv('data_track.csv', 'try.csv')
print(df)
ci.Read_csv.database_check(df)


conn = db_query.connect_db('status/status.db')
cursor = conn.cursor()

cursor.execute("""SELECT * FROM Status WHERE COMPOUND='TiO2' """)
#cursor.execute("""SELECT name FROM sqlite_schema WHERE type='Table' """)
ciao = cursor.fetchall()
print(ciao)

# print(df)
