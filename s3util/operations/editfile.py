import os
from s3util.utils.pathparser import pathparser

def editfile(path,client):
    [bucket, directory, incompletepath]= pathparser(path[0])
    try:
        client.download_file(bucket,directory+incompletepath,'/tmp/'+incompletepath)
    except:
        print("File doesn't exit "+directory+incompletepath+ " on s3, enter y or yes if you want to create the file")
        ans = input()
        if ans == 'y' or ans == 'yes':
            pass
        else:
            return 0
    try:
        os.system("vim %s" % "/tmp/"+incompletepath)
        client.upload_file('/tmp/'+incompletepath,bucket,directory+incompletepath)
        os.remove('/tmp/'+incompletepath)
    except:
        print("vim not found")
    