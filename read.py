
def read_text_without_pandas():
    
    p=open("/home/az2/s.txt","r")
    k=0
    for c in p:
        k=k+1
##        print(c)
##        if k == 6:
##            print('\n')
##            print('\n')
##            break
        
    p.close()
    print ('no of rows:  ', k/1000000,' Millions')
    print('\n')


def with_pandas():
    import pandas as pd
    
    data = pd.read_csv("/home/az2/s.txt",delimiter=";")
##    data = pd.read_csv("/home/az2/s.txt",delim_whitespace=True)
    print(data.tail())
    print('\n')
    print('\n')
    print(data.shape)


read_text_without_pandas()
with_pandas()
