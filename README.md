# Google-Drive-utility
## How to Use
Documentation at qiita
* [qiita](https://qiita.com/hrnckmr/items/e2fd307566580d0cae65)

from google colaboratory, you can upload json file as following
```
#file_upload_dialog
import google.colab.files as ggl
fname=ggl.upload()
print(fname)
#print_name
fname = [k for k in fname.keys()][0]
print(fname)
#change_the_json_name
import os
os.rename(fname,'client_secret.json')
```
#to use api you need "service" 
#create by following script
```
#service
from gutil import gutil
service = gutil.service()
```

#you can upload file in current directory (file name:sample.png),  
#to google drive(folder name: colab_temp)  
#like following
```
import subprocess
subprocess.Popen(["python", "./gutil/SmplUpld.py", "colab_temp", "sample.png",])
```
