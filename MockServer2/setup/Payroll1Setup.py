import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    try:
        conn = sqlite3.connect('Payroll.db')
        print(sqlite3.version)
    except Error as e:
        print(e)
    else:
        conn.close()

conn = sqlite3.connect(
    'Payroll.db')
conn.execute('create table employee(id integer primary key,'+
'name varchar(20),notes varchar(100),rvv integer)')
conn.execute('create table post(empid references employee,efrom date, '+
'grade varchar(4),manager references employee,rvv integer)')
conn.execute('create table holiday(empid references employee,hfrom date,'+
' hto date, agreed date,rvv integer)')
conn.execute('CREATE TABLE RVV(seq INTEGER)')
conn.execute('CREATE TABLE USER(uname VARCHAR(20) PRIMARY KEY ,password VARCHAR(20))')
conn.execute("INSERT INTO EMPLOYEE VALUES(1562,'John Black','Sales',1)")
conn.execute("INSERT INTO EMPLOYEE VALUES(1567,'Mary White','Finance',2)")
conn.execute("INSERT INTO EMPLOYEE VALUES(1569,'Paul Green','HR',3)")
conn.execute("INSERT INTO POST VALUES(1562,'2012-02-01','A1',1569,4)")
conn.execute("INSERT INTO POST VALUES(1562,'2012-04-01','A2',null,5)")
conn.execute("INSERT INTO POST VALUES(1567,'2012-02-01','B1',1569,6)")
conn.execute("INSERT INTO POST VALUES(1569,'2012-02-01','A2',null,7)")
conn.execute("INSERT INTO HOLYDAY VALUES(1567,'2012-03-02','2012-03-07'," + "'2012-02-05',8)")
conn.execute("INSERT INTO HOLYDAY VALUES(1569,'2012-04-04','2012-04-18'," + "null,9)")
conn.execute("INSERT INTO RVV VALUES(10)")
conn.execute("INSERT INTO USER VALUES('aUser','whosOk')")
conn.commit()
print('Done')


# if __name__ == '__main__':
#     create_connection()