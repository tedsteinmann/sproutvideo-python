# pip install requests
# pip install git+https://github.com/gregmccoy/sproutvideo-python@master

#https://stackoverflow.com/questions/8247605/configuring-so-that-pip-install-can-work-from-github
from sprout.client import SproutClient
import json

def getLinks(token, tags):
    sprout = SproutClient(token)
    video_data = sprout.tag.get()
    # writeJSONfile(video_data,'video_data.json')
    videos = {}
    for tag in tags:
        videos[tag] = getVideosByTag(video_data, tag)

    writeJSONfile(videos,'videos.json')
    return videos

def getVideosByTag(json_obj, name):
    dict = [json_obj][0]['tags']
    for entry in dict:
        if entry['name'] == name:
            return entry

def writeJSONfile(json_obj,file_name):
    # write videos to file
    # https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
    with open(file_name, 'w') as outfile:
        json.dump(json_obj, outfile, sort_keys=True, indent=4)
