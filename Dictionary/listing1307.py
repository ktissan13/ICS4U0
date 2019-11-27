english_dutch = { "last":"laatst", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal", "saw":
"zaag", "first":"eerst", "performance":"optreden", "of":"van",
"a":"een", "new":"nieuw", "symphony":"symphonie", "by":"bij",
"one":"een", "world":"wereld", "leading":"leidend", "modern":
"modern", "composer":"componist", "composers":"componisten",
"two":"twee", "shed":"schuur", "sheds":"schuren" }

sentence = "Last week The Royal Festival Hall saw the first \
performance of a new symphony by one of the world ' s leading \
modern composers , Arthur \"Two-Sheds\" Jackson."

sentence_list = sentence.split(' ')
final_sentence = ''

for word in sentence_list:
    if '-' in word:
        temp = word.split('-')
        for index in range(len(temp)):
            wrd = temp[index]
            if ('"') in word and index == 0:
                final_sentence = final_sentence + '"'
                wrdf = wrd.replace('"','')
                if wrdf.lower() in english_dutch:
                    final_sentence = final_sentence + english_dutch[wrdf.lower()]
            elif ('"') in word and index == 1:
                final_sentence = final_sentence + '-'
                wrdf = wrd.replace('"','')
                if wrdf.lower() in english_dutch:
                    final_sentence = final_sentence + english_dutch[wrdf.lower()]
        final_sentence = final_sentence + '" '

    elif word.lower() in english_dutch:
        final_sentence = final_sentence + english_dutch[word.lower()] + ' '
    else:
        final_sentence = final_sentence + word + ' '

print(final_sentence)
