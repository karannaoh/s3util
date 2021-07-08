def pathparser(path):
    paths = path.split('/')
    bucketname=''
    dir=''
    rest=''
    if(len(paths))>3:
        bucketname=paths[2]
        dir='/'.join(paths[3:-1])
        dir=dir+'/'
        rest=paths[-1]
    else:
        pass
    return[bucketname,dir,rest] 