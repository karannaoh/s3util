
import os
from s3util.utils.pathparser import pathparser

def printfile(path,client,recusive):
    files=[]
    [bucket, directory, incompletepath]= pathparser(path[0])
    if(recusive):
        if(directory=='/'):
            content = client.list_objects(Bucket=bucket)['Contents']
        else:
            content = client.list_objects(Bucket=bucket, Prefix=directory+incompletepath)['Contents']
        for key in content:
            files.append(key['Key'])
    else:
        files.append(directory+incompletepath)
    if(len(files)>15):
        print(str(len(files)) + " files present, still want to continue?(Y/N)")
        ans=input()
        if(ans=='Y'):
            pass
        else:
            return 0
    for count_file in files:
        try:
            client.download_file(bucket,count_file,'/tmp/'+("_").join(count_file.split("/")))
        except:
            print("File doesn't exit "+count_file+ " on s3")
            return 0
        print("File Location: s3://"+bucket+count_file)
        f = open('/tmp/'+("_").join(count_file.split("/")))
        for line in f:
            print(line.rstrip("\n"))
        f.close()
        os.remove('/tmp/'+("_").join(count_file.split("/")))
