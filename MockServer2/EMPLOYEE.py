import Json

class EMPLOYEE:
 """Python class representing a row of the EMPLOYEE table"""
 def __init__(self):
     self.id = 0
     self.name = ''
     self.notes = ''
     self.rvv = 0
     return

 def _Find(id, conn):
     c = conn.cursor()
     x = c.execute('SELECT * FROM EMPLOYEE WHERE id=' + str(id))
     e = EMPLOYEE()
     Json.GetOne(x, e, c.fetchone())
     c.close()
     return e