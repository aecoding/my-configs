#!/usr/bin/env python
from sys import argv

try:
    if argv[1] == '-c':
        if argv[2]: 
            prefix=argv[2][0] == '-'
            print(prefix)
except:
    pass

question=input('Question:\n')
answer=input('Answer:\n')
something_wrong=input('Did you made any mistakes? ').lower()
if something_wrong == 'yes':
    option=input('Type \'q\' to question,  \'a\' to answer or \'c\' to continue without changes: ')
    if option.lower() == 'q':
        question=input('Question:')
    else:
        answer=input('Answer:')

if argv[1] == 'pt':
    newQuestion = question[:] + '<br/>'
    portuguese = open('/home/aedigo/.termanki/portuguese/raw_cards.txt', 'a')
    portuguese.write(question + '<br/> ')
    portuguese.write(answer + '<br/>\n')
    portuguese.close()

if argv[1] == 'en':
    newQuestion = question[:] + '<br/>'
    portuguese = open('/home/aedigo/.termanki/english/raw_cards.txt', 'a')
    portuguese.write(question + '<br/> ')
    portuguese.write(answer + '<br/>\n')
    portuguese.close()
print(question, answer, something_wrong)
