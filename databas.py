# This file needs to be executed once for creating database and table in it

# ⚪️ ---creating database and table----
import sqlite3

#⚪️ ---customer - database name-
conn=sqlite3.connect('customer.db') 
c=conn.cursor()

#⚪️ ---log_in-table name----
c.execute("""CREATE TABLE log_in(    
            name text,
            email text primary key,
            password text 
        )""")

conn.commit()
conn.close()

       