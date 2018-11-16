Load Google Drive CSV into Pandas DataFrame for Google Colaboratory




import tensorflow as tf
tf.test.gpu_device_name()
This loads up TensorFlow and displays what GPU is being used. If it returns nothing, go to Runtime -> Change Runtime Type, change Hardware accelerator to GPU and hit save. Then re-run the code above. The result should be:

'/device:GPU:0'
If so, you are ready to move on.

!pip install -U -q PyDrive
 
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
 
### 1. Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
The above code installs PyDrive which will be used to access Google Drive and kicks off the process to authorize the notebook running in the Google Colaboratory environment to touch your files. When it runs, you will be presented with a link to click on, which asks to verify Google Colab can have access to Google Drive and unique key. Enter the key back in the notebook.

file_list = drive.ListFile({'q': "'<FOLDER ID>' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
This code assumes your CSV files are in a folder. It will print out the files in a folder and their unique identifiers which will be used below. Replace <FOLDER ID> with the long string of numbers and letters in the URL of the folder in Google Drive. If the files are located at the top level of Google Drive, replace <FOLDER ID> with ‘root’. The output should look like:

title: train.csv, id: <TRAIN_FILE_ID>
title: test.csv, id: <TEST_FILE_ID>
The output will be a list of files in the specified folder and their ids.

train_downloaded = drive.CreateFile({'id': '<TRAIN_FILE_ID>'})
train_downloaded.GetContentFile('train.csv')
test_downloaded = drive.CreateFile({'id': '<TEST_FILE_ID>'})
test_downloaded.GetContentFile('test.csv')  
Now the files get pulled into Google Colab. GetContentFile saves the files in the local environment and sets the names of the files.

import pandas as pd
import numpy as np
df_train = pd.read_csv('train.csv')
df_train
Now comes the easy part. Since the files have been saved to the local environment, load up a saved file, by its filename, into a DataFrame and print out a few lines to verify.

df_test = pd.read_csv('test.csv')
df_test

https://drive.google.com/file/d/1rgcYeA0pJ8SH8ODvTBXE6LexeX8-v3vy/view


Source
[http://nali.org/](http://nali.org/load-google-drive-csv-panda-dataframe-google-colab/)