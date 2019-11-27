
wordlist = ["apple","durian","banana","durian","apple","cherry","cherry","mango","apple","apple","cherry","durian","banana","apple","apple","apple","apple","banana","apple"]
fruits = dict()

for fruit in wordlist:
    if fruit not in fruits:
        fruits[fruit] = wordlist.count(fruit)

print(fruits)
