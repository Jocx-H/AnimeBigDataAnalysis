import json
import codecs
import os

if __name__ == '__main__':
    with open("../data/anime_1.json", encoding="utf-8") as file:
        file_json = json.load(file)
    max_title = 1
    max_url = 1
    max_video_link = 1
    max_cover = 1
    for line in file_json:
        max_title = max([len(line['title']), max_title])
        max_video_link = max([len(line['video_link']), max_video_link])
        max_cover = max([len(line['cover']), max_cover])
    print("max_title: ", max_title)
    # print("max_url: ", max_url)
    print("max_video_link: ", max_video_link)
    print("max_cover: ", max_cover)

