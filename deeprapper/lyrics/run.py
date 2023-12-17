import json
import re
import os
from pypinyin import pinyin, lazy_pinyin
import pypinyin
from tqdm import tqdm

root_path = "/home/guest/r12922121/ADL_2023_NTU/final/lyrics"
singers = ["蛋堡", "MC_HotDog熱狗", "國蛋", "熊仔"]

for singer in singers:
    # find all directoryy in root_path
    singer_path = os.path.join(root_path, singer, 'album')
    song_list = [os.path.join(singer_path, o) for o in os.listdir(singer_path) if os.path.isdir(os.path.join(singer_path,o))]

    # open file in each directory in album list
    for song in song_list:
        lyric_path = os.path.join(song, 'lyric_with_beat.txt')
        with open(lyric_path, 'r', encoding='utf-8') as f:
            lyric = json.load(f)
        lyric_list = lyric['lyric']
        # remove all the beat in lyric_list
        for i in range(len(lyric_list)):
            
            lyric_list[i] = re.sub(r'\[\d+:\d+\.\d+\]', '', lyric_list[i])
            # delete all english words and whitespace and enter and punctuation
            lyric_list[i] = re.sub(r'[^\u4e00-\u9fa5]', '', lyric_list[i])
            lyric_list[i] = re.sub(r'[a-zA-Z]', '', lyric_list[i])
            # print(lyric_list[i])

        line_list = [s for s in lyric_list if s.strip()]
        # write file in album_path/lyric.json
        map_list = []
        for line in line_list:
            line = lazy_pinyin(line, style=pypinyin.FINALS)
            line = ' '.join(line)
            map_list.append(line)
        # print(line_list)
        # print(map_list)
        with open(os.path.join(song, 'lyric_with_beat.txt'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(line_list))
        with open(os.path.join(song, 'mapped_final_with_beat.txt'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(map_list))