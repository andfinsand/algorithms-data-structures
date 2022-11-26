# a hashmap designed for strings and tuples.

# put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # put method to insert key,value pairs

    def put(self, key, val):

        # hash function

        hashed_key = hash(key) % self.size

        # get index

        bucket = self.hash_table[hashed_key]

        # check if index exists

        found_key = False
        for index, ele in enumerate(bucket):
            ele_key, ele_val = ele

            if ele_key == key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    # get value method

    def get(self, key):

        # hash function

        hashed_key = hash(key) % self.size

        # get index

        bucket = self.hash_table[hashed_key]

        # check if index exists

        found_key = False
        for index, ele in enumerate(bucket):
            ele_key, ele_val = ele

            if ele_key == key:
                found_key = True
                break

        if found_key:
            return ele_val
        else:
            return -1

    # remove method

    def remove(self, key):

        # hash function

        hashed_key = hash(key) % self.size

        # get index

        bucket = self.hash_table[hashed_key]

        # check if index exists

        found_key = False
        for index, ele in enumerate(bucket):
            ele_key, ele_val = ele

            if ele_key == key:
                found_key = True
                break

        if found_key:
            bucket.pop(index)
        return

    # print method

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

# examples

# create array with 10 buckets
hashmap = HashMap(10)

# insert two key,value pairs and print hashmap
hashmap.put("test key" , "test value")
hashmap.put("test key two" , "test value two")
print(hashmap)

# return value of specific key

print(hashmap.get("test key"))

# remove specified key, value pair and print hashmap
hashmap.remove("test key two")
print(hashmap)