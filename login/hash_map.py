#0620 11.30 done
import hashlib

class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[]for _ in range(self.size)] #初始化二維數據結構 每行都是一個空列表

    def _hash_function(self, key):
        hash_object = hashlib.md5(key.encode())
        return int(hash_object.hexdigest(), 16) % self.size
    
    def set(self, key, value):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))
    
    def get(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError('key not found') #引發異常（Exception）的關鍵字 使用 raise 來主動引發異常，從而中斷正常的程序流程
    
    def remove(self, key):
        hash_index = self._hash_function(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return 
        raise KeyError('key not found')
    
hash_table = HashTable(10)

hash_table.set("apple", 3)
hash_table.set("banana", 2)
hash_table.set("cherry", 1)

print(hash_table.get("cherry"))  # 1
