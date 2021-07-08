import argparse
from s3util.utils.pathparser import pathparser

def listpath(path,client,recursive):
    [bucket, directory, incompletepath]= pathparser(path[0])
    if(recursive):
        if(directory=='/'):
            result = client.list_objects(Bucket=bucket)
        else:
            result = client.list_objects(Bucket=bucket, Prefix=directory)
    else:
        if(directory=='/'):
            result = client.list_objects(Bucket=bucket,Delimiter='/')
        else:
            result = client.list_objects(Bucket=bucket, Prefix=directory, Delimiter='/')
        
    allpath=[]
    if('CommonPrefixes' in result):
        pref = ['s3://'+bucket+'/'+i['Prefix'] for i in result['CommonPrefixes']]
        allpath=allpath+pref
    if 'Contents' in result:
        cont=['s3://'+bucket+'/'+i['Key'] for i in result['Contents']]
        allpath=allpath+cont
    for paths in allpath:
        print(paths)