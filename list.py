acronyms = ['LOL', 'IDK', 'SMH', 'TBH']
acronyms.append('STFU')
word = 'STFU'

if word in acronyms:
    print(word + ' is in the list')
else:
    print(word + 'is not in the list')

for acronym in acronyms:
    print(acronym)
    