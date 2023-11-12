'''
Case-study №4
Developers:
            Shishko S. 75%
            Kuznetsov N. 50%
'''
import random
with open('input.txt', encoding='utf8') as input_file:
    s = input_file.readlines()
    string_file = ''
    for i in s:
        string_file += i

    list_file = list(map(str, string_file.split()))
    number_of_sentences = int(list_file[0])

    words_pairs = {}
    for i in range(1, len(list_file)-1):
        words_pairs[list_file[i]] = list_file[i+1]

    text = ''
    while 1:
        keyword = random.choice(list(words_pairs.keys()))
        text += keyword + ' '
        if text.count('.') + text.count('!') + text.count('?') >= number_of_sentences:
            break
        text += words_pairs.get(keyword) + ' '
        if text.count('.') + text.count('!') + text.count('?') >= number_of_sentences:
            break
    with open('output.txt', 'w', encoding='utf8') as output_file:
        output_file.write(text)
