# Inheritance test Question 1
# Tissan Kugathas
# ICS4U0
# November 4 2019

# Document class that holds the information about the document
class Document:
    # constructor
    def __init__(self):
        self.words = 0

    # Changes the number of document words.
    def setWords(self, numWords):
        self.words = numWords

    # Calculates the number of pages.
    def calculatePages(self):
        WORDS_PER_PAGE = 300
        pages = self.words / WORDS_PER_PAGE
        if (self.words % WORDS_PER_PAGE > 0):
            pages += 1
        return(round(pages))

    # Returns the number of words in a document.
    def getWords(self):
        return(self.words)

    # Returns info about the document such as the number of words and pages
    def __repr__(self):
        return "The document has {} word(s) and {} page(s)".format(self.getWords(),self.calculatePages())

# Essay class that holds the info about the essat
class Essay(Document):

    # constructor
    def __init__(self,num):
        # minuminum number of words allowed
        self.MIN_WORDS = 1500
        # maximum number of words allowed
        self.MAX_WORDS = 3000
        # the number of words in the essay
        self.num_words = num
        # initializes the document class (aka the super class)
        super().__init__()
        # set the words variable in document to the number of words in the essay
        self.setWords(self.num_words)

    # Check if the essay meets the min word count and max word count
    def validLength(self):
        # if true then returns true
        if self.MIN_WORDS < self.num_words < self.MAX_WORDS:
            return True
        # if false then it will return false
        else:
            return False

    # Returns the info about the essay such as the number of words, pages, and if the essay has a valid length
    def __repr__(self):
        if self.validLength():
            return "This essay has {} word(s) and {} page(s) and it has a valid length".format(self.num_words, self.calculatePages())
        else:
            return "This essay has {} word(s) and {} page(s) and it does not have a valid length".format(self.num_words, self.calculatePages())

# This essay only has 1400 words
testcase_one = Essay(1400)
# This essay has 2000 words
testcase_two = Essay(2000)

# These return the info about the essay
print(testcase_one)
print(testcase_two)
