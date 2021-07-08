from s3util.utils.pathparser import pathparser
import os
import time
import boto3

def path_completer():
    def main(prefix, parsed_args, **kwargs):
        if(parsed_args.profile!=None):
            boto3.setup_default_session(profile_name=parsed_args.profile)
        client = boto3.client('s3')
        [bucket, directory, incompletepath]= pathparser(prefix)
        if(os.path.isfile("/tmp/"+("_").join((bucket+directory)[:-1].split("/"))) and time.time()-os.path.getmtime("/tmp/"+("_").join((bucket+directory)[:-1].split("/"))) < 20):
            file1 = open("/tmp/"+("_").join((bucket+directory)[:-1].split("/")), 'r')
            paths=file1.read()
            return tuple(paths.split("THEDELIMETER"))
        if(bucket==''):
            if(os.path.isfile("/tmp/listbuckets3"+str(parsed_args.profile)) and time.time()-os.path.getmtime("/tmp/listbuckets3"+str(parsed_args.profile)) < 3600):
                file1 = open("/tmp/listbuckets3"+str(parsed_args.profile), 'r')
                paths=file1.read()
                return tuple(paths.split("THEDELIMETER"))
            res= client.list_buckets()['Buckets']
            ret=['s3://'+ buck['Name'] for buck in res]
            f = open("/tmp/listbuckets3"+str(parsed_args.profile), 'w')
            s = "THEDELIMETER".join(ret)
            f.write(s)
            return tuple(ret)
        if(directory=='' or directory=='/'):
            result = client.list_objects(Bucket=bucket, Delimiter='/')
        else:
            result = client.list_objects(Bucket=bucket, Prefix=directory, Delimiter='/')
        allpath=[]
        if('CommonPrefixes' in result):
            pref = ['s3://'+bucket+'/'+i['Prefix'] for i in result['CommonPrefixes']]
            allpath=allpath+pref
        if 'Contents' in result:
            cont=['s3://'+bucket+'/'+i['Key'] for i in result['Contents']]
            allpath=allpath+cont
        f = open("/tmp/"+("_").join((bucket+directory)[:-1].split("/")), 'w')
        s = "THEDELIMETER".join(allpath)
        f.write(s)
        return tuple(allpath)
    return main