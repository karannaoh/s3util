import argparse
from s3util.utils.pathparser import pathparser

def removefiles(paths,client,recursive):
    
    if(recursive):
        deletelist=[]
        for path in paths:
            [bucket, directory, incompletepath]= pathparser(path)
            operation_parameters = {'Bucket': bucket,
                        'Prefix': directory+incompletepath}
            object_response_paginator = client.get_paginator('list_objects_v2')
            
            for object_response_itr in object_response_paginator.paginate(**operation_parameters):
                if 'Contents' in object_response_itr:
                   deletelist.extend([{"Key":objects['Key']} for objects in object_response_itr['Contents']])
        print(len(deletelist)," objects will be deleted enter (Y/yes) to continue?")
        inp=input()
        if(inp=="Y" or inp=="yes"):
            if(len(deletelist)):
                for i in range(0, len(deletelist), 1000):
                    response = client.delete_objects(
                        Bucket=bucket,
                        Delete={
                            'Objects': deletelist[i:i+1000],
                            'Quiet': True
                        }
                    )
        else:
            print("quiting delete .......")
            return 0
    else:
        for path in paths:
            [bucket, directory, incompletepath]= pathparser(path)
            deletepath=[{"Key":(directory+incompletepath).strip("/")}]
            try:
                response = client.delete_objects(Bucket=bucket,Delete={'Objects': deletepath,'Quiet': True})
            except:
                print("Can not delete path ",deletepath)