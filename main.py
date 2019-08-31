from WordFinder import WFinder #Imports the WordFinder class
from DictionaryHashTable import DictHashTable

wf = WFinder() #Creates a new instance of WordFinder
ht = DictHashTable(100)

for i in range(100):
    ht.addItem(str(i))

print(ht.isInTable("124"))