"""
From CTCI

LRU Cache: Design and build a "least recently used" cache, which evicts the least recently used item.
The cache should map from keys to values (allowing you to insert and retrieve a value associ­ ated
with a particular key) and be initialized with a max size. When it is full,
it should evict the least recently used item.

"""

"""
From Leet code

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair 
to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?

"""

# normal first method My method

def lru_cache(keys_list):
    capacity = 4
    cache = dict()
    size = len(cache)
    age = 0
    min = 0

    for process in keys_list:
        if process in cache:
            age += 1
            cache[process] = age
        else:
            if size < capacity:
                #print(size)
                size += 1
                age += 1
                cache[process] = age
            else:
                min = float("inf")
                for key, value in cache.items():
                    if value < min:
                        min = value
                for key, value in cache.items():
                    if value == min:
                        remove_key = key
                        break
                del cache[key]
                age += 1
                cache[process] = age

    return cache

print(lru_cache([1,2,3,4,5,2,4,6]))



