# a hashmap designed for integers.

# put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    # hash function

    def getBucket(self, key):
        return self.buckets[key % self.size]

    # check if index exists

    def checkIndex(self, bucket, key):
        for index, (k , v) in enumerate(bucket):
            if k == key:
                return index
        return -1

    # put method to insert key,value pairs

    def put(self, key, val):
        bucket = self.getBucket(key)
        index = self.checkIndex(bucket, key)
        if index != -1:
            bucket[index][1] = val
        else:
            bucket.append([key , val])

    # get value method

    def get(self, key):
        bucket = self.getBucket(key)
        index = self.checkIndex(bucket, key)
        if index == -1:
            return -1
        return bucket[index][1]

    # remove method

    def remove(self, key):
        bucket = self.getBucket(key)
        index = self.checkIndex(bucket, key)
        if index == -1:
            return
        del bucket[index]

    def __str__(self):
        return "".join(str(item) for item in self.buckets)

# examples

# create array with 10 buckets
hashmap = HashMap(10)

# insert two key,value pairs and print hashmap
hashmap.put(1, 1)
hashmap.put(2, 2)
print(hashmap)

# return value of specific key

print(hashmap.get(1))

# # remove specified key, value pair and print hashmap
hashmap.remove(2)
print(hashmap)