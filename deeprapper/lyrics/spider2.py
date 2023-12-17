import requests
import urllib.parse
import re
from bs4 import BeautifulSoup
from spider import get_lyric
import json
from tqdm import tqdm
import os

root_path = "/home/guest/r12922121/ADL_2023_NTU/final/lyrics"
URL_ROOT = 'http://mojim.com/'
# singer = ["蛋堡", "MC_HotDog熱狗", "國蛋", "熊仔", "瘦子",\
#           "OZI", "Leo王", "大支", "頑童", "呂士軒",\
#           "高爾宣", 'gummyB', '阿法', '李英宏', 'wannasleep']

singer = ["蛋堡", "MC_HotDog熱狗", "國蛋", "熊仔"]
url = ["https://mojim.com/twh107409.htm", "https://mojim.com/twh101024.htm", "https://mojim.com/twh168202.htm",\
       "https://mojim.com/twh148382.htm"]

# , "https://mojim.com/twh229662.htm", "https://mojim.com/twh219438.htm",\
#        "https://mojim.com/twh172422.htm","https://mojim.com/twh102246.htm", "https://mojim.com/twh131970.htm",\
#        "https://mojim.com/twh216802.htm","https://mojim.com/twh221257.htm", "https://mojim.com/twh246472.htm",\
#         "https://mojim.com/twh230273.htm", "https://mojim.com/twh167766.htm", "https://mojim.com/twh236708.htm"]
# len(url)

for i in range(len(url)):
    data=[]
    url_list=[]
    singer_path = os.path.join(root_path, singer[i])
    os.makedirs(singer_path, exist_ok=True)
    album_path = os.path.join(singer_path, "album")
    os.makedirs(album_path, exist_ok=True)

    response = requests.get(url[i])
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    target_links = soup.find_all('a', title=lambda title: title and " 歌詞" in title)

    for link in target_links:
        url[i] = urllib.parse.urljoin(URL_ROOT, link.get('href'))
        url_list.append(url[i])

    for link in tqdm(url_list):
        # append if get_lyric(url) is not None
        if get_lyric(link) is not None:
            data.append(get_lyric(link))
            song_path = os.path.join(album_path, data[-1]['name'])
            os.makedirs(song_path, exist_ok=True)
            # write file in album_path/lyric.json
            with open(os.path.join(song_path, 'lyric_with_beat.txt'), 'w', encoding='utf-8') as f:
                json.dump(data[-1], f, ensure_ascii=False, indent=4)
