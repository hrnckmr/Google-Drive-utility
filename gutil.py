#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from apiclient.http import MediaIoBaseDownload
from httplib2 import Http
from oauth2client import file, client, tools
from oauth2client.tools import argparser, run_flow
import os
import sys
import io

msg='''
gutil ver4
Call "service = gutil.service()" and
get Resource in module googleapiclient.discovery object
'''
print(msg)

def service():
    '''
    Setup the Drive v3 API
    google Google Drive REST API Overview
    https://developers.google.com/drive/v3/web/about-sdk
    quick start for python
    https://developers.google.com/drive/v3/web/quickstart/python
    About Authorization
    https://developers.google.com/drive/v2/web/about-auth
    '''
    sys.argv=[]
    args = argparser.parse_args()
    args.noauth_local_webserver = True
    
    SCOPES = 'https://www.googleapis.com/auth/drive'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store,args)
    service = build('drive', 'v3', http=creds.authorize(Http()))
    return service

def gquery(service,query="mimeType='image/jpeg'"):
    '''
    file.list
    https://developers.google.com/drive/v3/web/search-parameters
    '''
    page_token = None
    gquery=[]
    cnt=0
    while True:
        response = service.files().list(q=query,spaces='drive',fields='nextPageToken, \
        files(id, name)',pageToken=page_token).execute()
        for file in response.get('files', []):
            # Process change
            print ('Found file: %s (%s)' % (file.get('name'), file.get('id')))
            gquery.append([cnt,file.get('name'), file.get('id')]) 
            cnt=cnt+1
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    return gquery

def gprint(service, file_id):
    """Print a file's metadata.    
    Args:
    service: Drive API service instance.
    file_id: ID of the file to print metadata for.
    """
    file = service.files().get(fileId=file_id).execute()
    return file

#file upload
def gupload(service,filepath,id=[]):
    '''
    upload to gdrive
    arg
    filepath: path of the file to upload
    id: The IDs of the parent folders which contain the file.
        If not specified as part of a create request, 
        the file will be placed directly in the user's My Drive folder. 
    '''
    file_metadata = {'name': os.path.basename(filepath),'parents':[id]}
    media_body = MediaFileUpload(filepath)
    file = service.files().create(body=file_metadata,media_body=media_body).execute()
    print('done')

def gdownload(service,id,path='./'):
    '''
    download from gddrive
    '''
    fname=service.files().get(fileId=id).execute()["name"]
    request = service.files().get_media(fileId=id)
    fh = io.FileIO(path+fname,'wb')
    downloader = http.MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print ("Download %d%%." % int(status.progress() * 100))
