import sqlite3

connection = sqlite3.connect("../resources/data.db")
cursor = connection.cursor()

# cursor.execute("SELECT * FROM sqlite_master WHERE type='table'")
# print(cursor.fetchall()) # => ('table', 't_person', 't_person', 56, 'CREATE TABLE "t_person" (\n\t"Id"\tINTEGER,\n\t"salutation"\tTEXT,\n\t"first_name"\tTEXT,\n\t"last_name"\tTEXT,\n\t"date_of_birth"\tNUMERIC,\n\t"is_vip"\tINTEGER,\n\t"salary"\tINTEGER,\n\t"date_of_creation"\tNUMERIC,\n\t"username"\tTEXT,\n\t"password"\tTEXT,\n\tPRIMARY KEY("Id")\n)')]

cursor.execute("""
  update t_person
     set first_name = substr(first_name, 1, 1) || '*********'
        ,last_name = abs(random()) % 1000000000 + 1000000000
        ,date_of_birth = substr(date_of_birth, 1, 4)
        ,salary = case when salary is null then null when salary < 50000 then 'low' when salary < 100000 then 'medium' else 'high' end
        ,username = null
        ,password = null
        ,is_vip = null
""")

# cursor.execute("select * from t_person")
# print(cursor.fetchall())

# connection.rollback()
connection.commit()
connection.close()
