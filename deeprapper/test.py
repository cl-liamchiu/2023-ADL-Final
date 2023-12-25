import opencc
converter = opencc.OpenCC('s2t.json')
a = converter.convert(['汉字', '汉字'])  # 漢字
print(a)