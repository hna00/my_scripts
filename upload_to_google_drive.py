#docs: https://pythonhosted.org/PyDrive/
#https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf // place clients_secret.json in same directory

from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

  
# Below code does the authentication
# part of the code
gauth = GoogleAuth()
  
# Creates local webserver and auto
# handles authentication.
gauth.LocalWebserverAuth()       
drive = GoogleDrive(gauth)
   
# replace the value of this variable
# with the absolute path of the uploaded file
path_to_file = "/home/kali/fu/touch.txt"
title=path_to_file.split('/')[-1]

f = drive.CreateFile({'title': title})
f.SetContentFile(path_to_file)
f.Upload()
permission = f.InsertPermission({
                        'type': 'anyone',
                        'value': 'anyone',
                        'role': 'reader'})

print('URL to access the file from google drive: ' + f['alternateLink'])  # Display the sharable link.
f= None