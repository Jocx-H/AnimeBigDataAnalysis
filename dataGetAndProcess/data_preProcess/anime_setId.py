import json
import codecs
import os

if __name__ == '__main__':
    with open("../data/anime+intro.json", encoding="utf-8") as file:
        file_json = json.load(file)
    json_file = codecs.open('../data/anime_1.json', 'w+', encoding='UTF-8')
    json_file.write('[\n')
    id = 1
    max_intro = 1
    for line in file_json:
        json_data = line
        json_data['id'] = int('1' + str(id))
        id += 1
        json_data['introduce'] = json_data['introduce'] if len(json_data['introduce']) <= 300 else \
            (json_data['introduce'][: 300] + "...")
        max_intro = max([len(line['introduce']), max_intro])
        json_data = json.dumps(json_data, ensure_ascii=False)
        json_file.write('\t' + json_data + ',\n')
    print("max_intro: ", max_intro)
    json_file.seek(-2, os.SEEK_END)
    json_file.truncate()
    json_file.write('\n]')
    json_file.close()
