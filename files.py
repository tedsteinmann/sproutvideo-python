# https://stackoverflow.com/questions/11131810/passing-a-variable-in-url
from pathlib import Path
import requests
import os.path

def downloadFile(name,theurl,file_path):
    print(theurl)
    r=requests.get(theurl)
    completeName = os.path.expanduser(file_path + "/" + name + ".mp4")
    downloadPath = Path(completeName)
    if not downloadPath.is_file():
        print("****Connected****")
        print("Downloading: ",name)
        f=open(completeName,'wb');
        print("Donloading ",name," ......")
        for chunk in r.iter_content(chunk_size=255):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
        print("Done")
        f.close()
    else:
        print("Skipped file: " + name + " because it already existed.")
