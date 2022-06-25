"""
@Author: CloudAndMist
"""
import json
import codecs
import os

if __name__ == '__main__':
    with open("../data/preData/preNovel.json", encoding="utf-8") as file:
        file_json = json.load(file)
    json_file = codecs.open('../data/novel.json', 'w+', encoding='UTF-8')
    json_file.write('[\n')
    id = 1
    for line in file_json:
        json_data = line
        json_data['id'] = int('3' + str(id))
        id += 1
        json_data = json.dumps(json_data, ensure_ascii=False)
        json_file.write('\t' + json_data + ',\n')
    json_file.seek(-2, os.SEEK_END)
    json_file.truncate()
    json_file.write('\n]')
    json_file.close()
