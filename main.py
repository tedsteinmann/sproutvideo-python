from configparser import ConfigParser
from pathlib import Path
from files import downloadFile
from pandas import DataFrame
import json

from sprout.client import SproutClient
from links import getLinks
from videos import getVideos

config = ConfigParser()
config.read('config.ini')
token = config.get('auth', 'token')
# ----------
# config.ini - format
# [auth]
# token = YOUR API TOKEN
# ----------
tags = ['NAMP','GIF IV']
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
    data_file = getVideos(video_json, token)

# Read data from file system
data_file = DataFrame.from_csv(video_data_file, sep='\t')
    # get videos from API

# get videos from file
for index, row in data_file.iterrows():
    #print(row.name,row[0],row[4])
    file_path = "~/Box Sync/NAMP-GIF/" + row.name
    print(row[0],row[4],file_path)
    # downloadFile(row[0],row[4],file_path)