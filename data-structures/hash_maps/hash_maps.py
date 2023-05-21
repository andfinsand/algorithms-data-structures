class HashMap:
    # initialize hash map class
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_bucket()

    def create_bucket(self): # method to create empty array
        return [[] for _ in range(self.size)]

    # insert value into hashmap
    def insert(self, key, value):

        hashed_key = hash(key) % self.size # hash function

        bucket = self.hash_table[hashed_key] # get bucket (index)

        found_key = False
        for index, record in enumerate(bucket): # check if bucket key is same as insert key
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break
        if found_key: # if bucket has same key, update key-value
            bucket[index] = (key, value)
        else: # otherwise append new key-value
            bucket.append((key, value))

    # print items of hashmap
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

# Tests

hash_map = HashMap(5)
hash_map.insert("Jugghead" , "Jones")
hash_map.insert("Donald" , "Duck")
print(hash_map)
