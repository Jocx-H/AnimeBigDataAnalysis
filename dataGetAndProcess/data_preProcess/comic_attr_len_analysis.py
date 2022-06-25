"""
@Author: CloudAndMist
"""
import json
import codecs
import os

if __name__ == '__main__':
    with open("../data/comic.json", encoding="utf-8") as file:
        file_json = json.load(file)
    max_title = 1
    max_url = 1
    max_video_link = 1
    max_cover = 1
    for line in file_json:
        max_title = max([len(line['title']), max_title])
        max_url = max([len(line['url']), max_url])
    print("max_title: ", max_title)
    print("max_url: ", max_url)

