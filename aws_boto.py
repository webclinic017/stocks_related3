import pandas as pd

def f2_list_all_files_folders():
    

    import boto3
    import pandas as pd

    client = boto3.client('s3')
    response = client.list_buckets()
    print(type(response))
    pp=[]
    pg=[]

    s3 = boto3.resource('s3')


    m=1

    for bucket in response["Buckets"]:
        
        print('\n\n')
        print('************************************************************************')
        print(m,')  ',bucket['Name'])
        
        my_bucket = s3.Bucket(bucket['Name'])
        k=1
        for file in my_bucket.objects.all():
##            if m==19:
                
                
                print('   ',k,'        ',' ---->   ', file)
                k=k+1
    ##        print(file.key)
            
        m=m+1 
##        print('\n\n','Total no of files in this bucket ', k) 






    print(pp)
    print('\n\n')
    ##obj = response.get_object(Bucket='bucket', Key='key')
    ##df = pd.read_csv(obj['Body'])


    ##df=pd.DataFrame.from_dict(response)
    ##print(df)  bucket['CreationDate']


def f2_how_many_buckets():
    

    import boto3
    import pandas as pd

    client = boto3.client('s3')
    response = client.list_buckets()
    print(type(response))
    pp=[]
    pg=[]

    s3 = boto3.resource('s3')

    k2=1
    m=1

    for bucket in response["Buckets"]:
        
##        print('\n\n')
##        print('************************************************************************')
##        print(m,')  ',bucket['Name'])
        
        my_bucket = s3.Bucket(bucket['Name'])
        k=1
        for file in my_bucket.objects.all():   
##                print('   ',k,'        ',' ---->   ', file)
                k=k+1
                k2=k2+1
          
        m=m+1
    print('No of buckets:                      ',m)
    print('No of files in all buckets/total:   ',k2)

##    print(pp)
##    print('\n\n')




def f3():
    import boto3
    import pandas as pd
    from s3fs.core import S3FileSystem

##    pp=[]
##    dd=[]
##
##    s3 = boto3.client('s3')
##    obj = s3.get_object(Bucket='p60', Key='fake_46.csv')
##    print(type(obj))
##
##    df = pd.read_csv(obj['Body'])
##    print(df)


    import s3fs
    import pandas as pd
    s3 = s3fs.S3FileSystem(profile='azhar145')

##    csv_string = body.read().decode('utf-8')
    df=pd.read_csv(s3.open('s3://p57/fake_46.csv', sep="\s+"))


    print(df)

def f4_delete_all_files_in_folder():
    import boto3    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('p56')
    # suggested by Jordon Philips 
    bucket.objects.all().delete()

def f5_delete_bucket():
    import boto3   
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('p56')
##    bucket.objects.filter(Prefix="delete22vcv/").delete()
    bucket.delete()

f2_how_many_buckets()
##f4_delete_all_files_in_folder()
##f5_delete_bucket()
##f2_list_all_files_folders()
