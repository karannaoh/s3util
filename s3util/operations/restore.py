from s3util.utils.pathparser import pathparser

def restore(path,client,recursive,days):
    if(days==None):
        print("--days is required for restore operation")
        return 0
    paths=[]
    for li in path:
         paths.append(pathparser(li))
    if(recursive):
        object_response_paginator = client.get_paginator('list_object_versions')
        for bucket, directory, incompletepath in paths:
            operation_parameters = {'Bucket': bucket,
                        'Prefix': directory+incompletepath}
            for object_response_itr in object_response_paginator.paginate(**operation_parameters):
                if 'Versions' in object_response_itr:
                    for version in object_response_itr['Versions']:
                        try:
                            client.restore_object(
                                Bucket=bucket,
                                Key=version['Key'],
                                RestoreRequest={'Days': int(days),'Tier': 'Standard'}    
                            )
                        except Exception as ex:
                            template = "An exception of type {0} occurred. Arguments:\n{1!r}, path {2}"
                            message = template.format(type(ex).__name__, ex.args,"s3://"+bucket+"/"+version['Key'])
                            print(message)
    else:
        for bucket, directory, incompletepath in paths:
            client.restore_object(
                Bucket=bucket,
                Key=directory+incompletepath,
                RestoreRequest={'Days': days,'Tier': 'Standard'}    
            )
