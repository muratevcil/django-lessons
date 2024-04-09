import sqlite3
db = sqlite3.connect("projectDB.db")
cursor = db.cursor()
cursor.execute("""UPDATE users SET bölüm = "Bilgisayar"
 WHERE ad = 'Fatma' """)
db.commit()
db.close()