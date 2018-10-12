# https://stackoverflow.com/questions/11131810/passing-a-variable-in-url
import requests
import os.path

def downloadFile(name,theurl,file_path):
    r=requests.get(theurl)
    print("****Connected****")
    completeName = os.path.expanduser(file_path + "/" + name + ".mp4")
    f=open(completeName,'wb');
    print("Donloading ",name," ......")
    for chunk in r.iter_content(chunk_size=255):
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    print("Done")
    f.close()
