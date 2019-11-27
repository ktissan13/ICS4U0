text = "apple ,durian ,banana ,durian ,apple ,cherry ,cherry ,mango ," + \
"apple ,apple ,cherry ,durian ,banana ,apple ,apple ,apple ," + \
"apple ,banana ,apple"

words = text.split(' ,')
finaldict = dict()

for word in words:
    if word not in finaldict:
        finaldict[word] = words.count(word)

print(finaldict)
