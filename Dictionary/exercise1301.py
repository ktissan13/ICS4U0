text = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck , he would , as much as he could ,
And chuck as much as a woodchuck would
If a woodchuck could chuck wood."""

words = []

stat = dict()

colum = text.split('\n')

for sentence in colum:
    temp = sentence.lower().split(' ')
    words += temp

for word in words:
    word = word.replace('?','')
    word = word.replace('.','')
    if word not in stat and word != ',':
        stat[word] = words.count(word)

print(stat)
