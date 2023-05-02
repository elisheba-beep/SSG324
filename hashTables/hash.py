class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    #gets the hash vaue of a key
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash+=ord(char)
        return hash%self.MAX
    
    #creates a key/value pair
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
        
    #gives the value of a particular key
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    #deletes the key and value
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
        

myHash = HashTable()
myHash.__setitem__('Tomiwa', 21)
myHash.__setitem__('Sheba', 22)
print(myHash.__getitem__('Tomiwa'))
print(myHash.get_hash('Tomiwa'))
myHash.__delitem__('Tomiwa')
print(myHash.__getitem__('Tomiwa'))
