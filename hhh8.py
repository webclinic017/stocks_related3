import sys
import cx_Oracle
 
class Customer():    
   def createCustomer(self,fname):
       print ("name is %s" % fname)
       db = cx_Oracle.connect('system/12345678@localhost/XE' )
       cursor=db.cursor()
       cursor.execute("INSERT INTO telm  VALUES (fname)")
       db.commit()
 
fname=input("Enter your first name :")
c1=Customer();
c1.createCustomer(fname)
