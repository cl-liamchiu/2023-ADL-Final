import requests
import urllib.parse
import re
from bs4 import BeautifulSoup
URL_ROOT = 'http://mojim.com/'

def get_lyric(url):
    url = urllib.parse.urljoin(URL_ROOT, url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    lyric = soup.find('dl', 'fsZx1')
    a = re.compile('^\[\d+')
    
    lyric_list = list()
    if lyric is None:
        return None
    for string in lyric.stripped_strings:
        if string == '更多更詳盡歌詞 在' or string == '※ Mojim.com　魔鏡歌詞網' or string == '提供歌詞' or string == '感謝':
            continue
        if a.match(string):
            break
        lyric_list.append(string)

    singer = lyric_list.pop(0)
    name = lyric_list.pop(0)

    song_detail = {
        'singer':singer,
        'name':name,
        'lyric':lyric_list,
    }
    return song_detail
