import json
from collections import Counter

with open('newsafr.json', encoding='utf-8') as json_file_input:
    json_data = json.load(json_file_input)
    long_words_list = []
    for block in json_data["rss"]["channel"]["items"]:
        description_text = block['description'].strip().split(' ')
        for word in description_text:
            word_upper = word.upper()
            if len(word_upper) > 6:
                long_words_list.append(word_upper)
    long_words_dict = dict(Counter(long_words_list).most_common(10))
    print('ТОП 10 часто встречающихся слов больше 6 символов:')
    for key, value in long_words_dict.items():
        print(key, value)
