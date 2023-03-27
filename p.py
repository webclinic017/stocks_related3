#Step1

##from subprocess import Popen, PIPE, STDOUT
##import os
####
##from subprocess import Popen, PIPE
##
##cmd = 'cd /usr/lib/oracle/xe/app/oracle/product/10.2.0/server/bin && lsnrctl start'
##p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, close_fds=True)
##output = p.stdout.read()
##cmd = '/etc/init.d/oracle-xe start'
##p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
##output = p.stdout.read()

###########################33
##
import cx_Oracle
import os
##os.environ["LD_LIBRARY_PATH"] = '/home/az2/Downloads/instantclient_10_2'
##LD_LIBRARY_PATH = '/home/az2/Downloads/instantclient_10_2'
ip = '192.168.1.70'
port = '1521'
SID = 'karachi2'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)

db = cx_Oracle.connect("az2", "1", dsn_tns)

c = db.cursor()
##c.execute('SELECT owner, table_name FROM all_tables')
c.execute('SELECT count(table_name) FROM all_tables')
for row in c: print(row)
c.execute('SELECT distinct(owner) from all_tables')
for row in c: print(row)
##c.execute('select * from Z1 where rownum < 5')
##c.execute('select table_name from tabs')
##c.execute('SELECT table_name, owner FROM all_tables ORDER BY owner, table_name')
##for row in c: print(row[[0,1]])
##c.execute('CREATE USER fdd IDENTIFIED BY aafdd')
##c.execute('GRANT CONNECT TO azhar_3')
##c.execute('GRANT CONNECT, RESOURCE, DBA TO azhar_3')
##c.execute('GRANT CREATE SESSION GRANT ANY PRIVILEGE TO azhar_3')
##c.execute('GRANT UNLIMITED TABLESPACE TO azhar_3')
##c.execute('GRANT SELECT,INSERT,UPDATE,DELETE ON schema.books TO azhar_3')
##for row in c: print(row)

db.close()
