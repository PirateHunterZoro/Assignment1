"""
import MySQLdb

for python 3 i used mysql-connector.
"""
import mysql.connector

class db:
    def __init__(self):

        self.conn=mysql.connector.connect(user='root',password='umbreon1',host='localhost',database='Books')

        self.mycursor=self.conn.cursor()

    def create(self):
        self.__init__()
        self.mycursor.execute("DROP TABLE IF EXISTS users")

        sql = """CREATE TABLE users (
                  cust_id int(5) NOT NULL,
                  surname varchar(50),
                  firstname varchar(50),
                  initial char(1),
                  title_id int(3),
                  address varchar(50),
                  city varchar(50),
                  state varchar(20),
                  zipcode varchar(10),
                  country_id int(4),
                  phone varchar(15),
                  birth_date char(10),
                  PRIMARY KEY (cust_id)
                );"""

        self.mycursor.execute(sql)
        self.conn.close()

    def insert(self):
        self.__init__()
        sql = """INSERT INTO users VALUES 
        (1,'Rosenthal','Joshua','B',1,'34 Mellili Ln','Earlwood','VIC','6750',12,'(613)83008460','1969-01-26');"""
        try:
            # Execute the SQL command
            self.mycursor.execute(sql)
            # Commit your changes in the database
            self.conn.commit()
        except:
            # Rollback in case there is any error
            self.conn.rollback()

        self.conn.close()

    def select(self):
        self.__init__()
        sql = "SELECT * FROM users where cust_id=1"
        try:
            # Execute the SQL command
            self.mycursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = self.mycursor.fetchall()
            for row in results:
                cust_id = row[0]
                user_name = row[1]
                # Now print fetched result
                print(cust_id,user_name)
        except:
            print("Error: unable to fecth data")

        # disconnect from server
        self.conn.close()

    def update(self):
        self.__init__()
        sql = "UPDATE users SET firstname = 'Naveen' WHERE cust_id = 1"

        try:
            # Execute the SQL command
            self.mycursor.execute(sql)
            # Commit your changes in the database
            self.conn.commit()
        except:
            # Rollback in case there is any error
            self.conn.rollback()

        # disconnect from server
        self.conn.close()

    def delete(self):
        self.__init__()
        sql = "DELETE FROM users WHERE cust_id=1"
        try:
            # Execute the SQL command
            self.mycursor.execute(sql)
            # Commit your changes in the database
            self.conn.commit()
        except:
            # Rollback in case there is any error
            self.conn.rollback()

        # disconnect from server
        self.conn.close()


if __name__ == "__main__":
    d=db()
    d.create()
    d.insert()
    d.select()
    d.update()
    d.delete()






