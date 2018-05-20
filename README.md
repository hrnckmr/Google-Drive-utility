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
you should feed service to use api  
create service as following
```
#service
from gutil import gutil
service = gutil.service()
```

