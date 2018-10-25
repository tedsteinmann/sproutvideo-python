from pandas import DataFrame
from sprout.client import SproutClient
import json

file_name = "videos.tsv"

def getVideos(video_json, token, type):

    dict = [video_json][0]
    list=[]
    #loop over all videos
    try:
        for tag in dict:
            # print(group) #tag name
            videos = dict[tag]['videos'] #videos
            for video in videos:
                list.append(getVideoAttributesAsList(tag,video,token,type))
    except Exception as e:
        print("Video data API calls failed")
        print(e)
        return

    df = DataFrame(list) #not sure why there are weird headers.
    df.to_csv(file_name, sep='\t', encoding='utf-8', index=False, header=False)
    print('Printed ',file_name,' to local file system')
    return df

# Get videos
def getVideoAttributesAsList(tag,id, token, type):
    # TODO: this can probably be done better by reading from one object instead of calling the API
    sprout = SproutClient(token)
    video_data = sprout.video.get(id)

    list = []
    list.append(tag)
    list.append(video_data['title'])
    list.append(video_data['description'])
    list.append(video_data['created_at'])
    list.append(video_data['updated_at'])
    list.append(id)


    return list
