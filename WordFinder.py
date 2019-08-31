from DictionaryHashTable import DictHashTable

class WFinder:

    def __init__(self):
        f = open("wwfWords.txt", "r")
        dht = DictHashTable(10)

    def isWord(self, word):
        if (word=="cat"):
            return True
        return False