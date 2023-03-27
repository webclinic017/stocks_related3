

def mm():
    import os
    import os.path, time
    
    directory = r'C:\Users\aa300j\Downloads'
    
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                print('root   ', root,'  dirs ',dirs,' -----> ',file)
                print('\n')
                
##                print(os.path.join(root, file))
##                 (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
##                 print("last modified: %s" % time.ctime(mtime))

##                 print("last modified: %s" % time.ctime(os.path.getmtime(file)))
##                 print("created: %s" % time.ctime(os.path.getctime(file)))




def bb():
    import os

    ##user_input = input('What is the name of your directory')
    ##directory = os.listdir(user_input)
    directory = r'C:\Users\aa300j\Downloads'

    ##searchstring = input('What word are you trying to find?')
    searchstring ='ssh'

    for fname in directory:
        if os.path.isfile(user_input + os.sep + fname):
            # Full path
            f = open(user_input + os.sep + fname, 'r')

            if searchstring in f.read():
                print('found string in file %s' % fname)
            else:
                print('string not found')
            f.close()




################################
import os,time

directory = r'C:\Users\aa300j\Downloads'
text_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
print(text_files)

import glob
import pandas as pd
pd.set_option('display.width', 2000)
pd.set_option('display.max_seq_items',None)
pd.set_option('display.max_colwidth',None)
pd.set_option('display.max_rows', None)
files=[]
bb=[]
cc=[]

d2=[]
d3=[]
d4=[]
d5=[]
d6=[]
d7=[]

print('\n')
searchstring ='dlp'
zz=r'C:\Users\aa300j\Downloads\PEP\Connect_it_files\Azhar_connect_it_scripts\tt\mia2b (2)'
for file in glob.glob("C:/Users/aa300j/Downloads/**/*.py", recursive = True):
##for file in glob.glob(str(zz)+str('/**/*.xlsm'), recursive = True):    
    b=time.strftime('%Y-%m-%d %H:%M', time.localtime(os.path.getmtime(file)))
    c=time.strftime('%A', time.localtime(os.path.getmtime(file)))
##    print(file,'   ',b,'  ',c)
###########################################################################
    f=open(file)
    if str(searchstring) in f.read():
        d2.append('found string ')
        d3.append(searchstring)
        d4.append('-> ')
        d5.append(file)
        d6.append(b)
        d7.append(c)
##        print('found string %s [',searchstring,'] in file -----> %s' % file,'   ',b)
    f.close()
###########################################################################    
    files.append(file)
    bb.append(b)
    cc.append(c)

df2=pd.DataFrame([d2,d3,d4,d5,d6,d7]).T
df2.columns=['d2','d3','d4','d5','d6','d7']
df2['d6'] = pd.to_datetime(df2['d6'])
df2.sort_values(by='d6', inplace=True,ascending = False)
df2=df2[['d5','d6']]
print('search ---> [',searchstring,']')
print(df2)
print('\n\n')
    

df=pd.DataFrame([files,bb])
df=df.T
df.columns=['b','c']
print('\n\n')
print(df,' 44')
df['c'] = pd.to_datetime(df['c'])
df.sort_values(by='c', inplace=True,ascending = False)

print(df,' 55')
    

