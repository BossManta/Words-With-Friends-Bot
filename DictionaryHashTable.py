import math

class DictHashTable:

    #Constuctor takes in size of the hash table. 
    def __init__(self, tableSize):
        self.tableSize = tableSize
        self.table = [None]*tableSize
    

    #Hashes the item given to find its location in the hash table.
    def getTableLocation(self, item):
        return math.floor(abs(hash(item))/(10000000000000000000)*self.tableSize)


    #Adds new item to hash table.
    def addItem(self, item):
        loc = self.getTableLocation(item)
        if (self.table[loc]==None):
            self.table[loc]=[]

        self.table[loc].append(item)
        

    #Checks if item is inside hash table.
    def isInTable(self, item):
        loc = self.getTableLocation(item)
        if (self.table[loc]!=None):
            if (item in self.table[loc]):
                return True
        return False