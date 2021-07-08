import pdb
from s3util.operations.list import listpath
import argcomplete, argparse
from argcomplete.completers import ChoicesCompleter
from s3util.utils.pathcompleter import path_completer
from s3util.operations.editfile import editfile
from s3util.operations.printfile import printfile 
from s3util.operations.restore import restore
from s3util.operations.s3rm import removefiles
from s3util.operations.s3copy import copyfile
from s3util.operations.s3mv import movefile
import boto3
import os


def main():
    
    parser = argparse.ArgumentParser(prog ='s3util',description ='s3 utility to help with s3 operations')
    parser.add_argument('--profile', help ="options")
    parser.add_argument('action', type = str,help ='an integer for the accumulator',choices=['cat', 'ls', 'restore','vim','mv','rm','cp'])
    parser.add_argument('path', type = str,nargs='+',help ='an integer for the accumulator',default=[]).completer = path_completer()
    parser.add_argument('-r','--recursive', help ="options",action="store_true")
    parser.add_argument('--days', help ="options")
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    if(args.profile!=None):
      boto3.setup_default_session(profile_name=args.profile)
    client = boto3.client('s3')
    if(args.action=='cat'):
      printfile(args.path,client,args.recursive)
    elif(args.action=='ls'):
      listpath(args.path,client,args.recursive)
    elif(args.action=='restore'):
      restore(args.path,client,args.recursive,args.days)
    elif(args.action=='vim'):
      editfile(args.path,client)
    elif(args.action=='cp'):
      copyfile(args.path,client,args.recursive,args.profile)
    elif(args.action=='rm'):
      removefiles(args.path,client,args.recursive)
    elif(args.action=='mv'):
      movefile(args.path,client,args.recursive,args.profile)
    else:
      print("option not valid")