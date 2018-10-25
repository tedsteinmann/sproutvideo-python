'''
Author: @tedsteinmann
Description: Download videos from sprout video by tag
'''
import os
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
config = ConfigParser()
config.read('config.ini')
token = config.get('auth', 'token')

# ----------
# config.ini - format
# ----------
# [auth]
# token = YOUR API TOKEN
# [input]
# local_path = "~/Box Sync/NAMP-GIF/"
# tags = ['NAMP','GIF IV']
# type = 'hd' # type of download: source, hd or sd
# download_url = "https://sproutvideo.com/videos/"
# ----------

local_path = config.get('input', 'local_path')
# tags = config.get('input', 'tags')
tags = ['DHS']
type = config.get('input', 'type')
download_url = config.get('input', 'download_url')

# --------
# files below will be written to file system at root
videos_file = Path("videos.json")
video_data_file = Path("videos.tsv")

videos_file_completed = Path("videos.json.completed")
video_data_file_completed = Path("videos.json.completed")
# ----------

def getVideoData():

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
        return getVideos(video_json, token, type)
    else:
        print("Reading select video data from local file system.")
        return DataFrame.from_csv(video_data_file, sep='\t')

def downloadVideos(data_file,tags):

    #TODO: create directory(s) for videos to be downloaded to if doesn't exist
    try:
        # get videos from file
        for index, row in data_file.iterrows():
            file_path = local_path + "/" + row.name
            url = download_url + row[4] + "/download?type=" + type
            downloadFile(row[0],url,file_path)
    except Exception as e:
        print("Download of videos failed")
        print(e)
        return
    print("Successfully downloaded videos.")

print("Calling getVideosData()")
data_file = getVideoData()
print("------------------------------")
print("Calling downloadVideos()")
downloadVideos(data_file, tags)
archive = input('Archive data files? (y/n): ')
if archive == 'y':
    print("Renaming source files with 'completed_' prefix.")
    videos_file.rename(videos_file_completed)
    video_data_file.rename(video_data_file_completed)
