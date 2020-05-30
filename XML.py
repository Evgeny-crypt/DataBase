import xml.etree.ElementTree as ET
from collections import Counter


parser = ET.XMLParser(encoding='UTF-8')
tree = ET.parse('newralf.xml', parser)
root = tree.getroot()
path_item = root.findall('channel/item')
long_words_list = []

for item in path_item:
    description_text = item.find('description').text.strip().split(' ')
    for word in description_text:
        word_t = word.upper()
        if len(word_t) > 6:
            long_words_list.append(word_t)
long_words_dict = dict(Counter(long_words_list).most_common(10))
print('ТОП 10 часто встречающихся слов больше 6 символов:')
for key, value in long_words_dict.items():
    print(key, value)
