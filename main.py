'''
Author: @tedsteinmann
Description: Download videos from sprout video by tag
'''
from configparser import ConfigParser
from pathlib import Path
from files import downloadFile
from pandas import DataFrame
import json

from sprout.client import SproutClient
from links import getLinks
from videos import getVideos
# Customize these
# ---------------
local_path = "~/Box Sync/NAMP-GIF/"
tags = ['NAMP','GIF IV']
type = 'source' # type of download: source, hd or sd
download_url = "https://sproutvideo.com/videos/"
# ---------------
config = ConfigParser()
config.read('config.ini')
token = config.get('auth', 'token')
# ----------
# config.ini - format
# [auth]
# token = YOUR API TOKEN
# ----------
videos_file = Path("videos.json")
video_data_file = Path("videos.tsv")
# ----------

# Get videos
if videos_file.is_file():
    # file exists
    print("Reading videos from local file.")
    with open(videos_file) as json_data:
        video_json = json.load(json_data)
else:
    # get links from API
    print("Getting videos from Sprout API ...")
    video_json = getLinks(token, tags)
    print("File videos.json written to local file system.")

if not video_data_file.is_file():
    # write the data file if it doesn't exist
    print("Reading select video data from API.")
    # Read data from file system
    data_file = getVideos(video_json, token, type)
else:
    # get videos from API
    data_file = DataFrame.from_csv(video_data_file, sep='\t')

# get videos from file
for index, row in data_file.iterrows():
    #print(row.name,row[0],row[4])
    file_path = local_path + "/" + row.name
    url = download_url + row[4] + "/download?type=" + type
    #print(url)
    downloadFile(row[0],url,file_path)
