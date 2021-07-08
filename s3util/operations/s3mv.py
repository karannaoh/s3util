import os
from s3util.utils.pathparser import pathparser


def movefile(paths,client,recursive,profile):
    if(len(paths)!=2):
        print("2 paths are expected")
        return 0
    try:
        if(recursive):
            if(profile==None):
                os.system("aws s3 mv "+paths[0]+" " +paths[1]+" --recursive")
            else:
                os.system("aws s3 mv "+paths[0]+" " +paths[1]+" --profile "+profile+" --recursive")
        else:
            if(profile==None):
                os.system("aws s3 mv "+paths[0]+" " +paths[1]+" --profile "+profile)
    except:
        print("Please install aws cli")