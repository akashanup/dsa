"""
# Intuition
To implement a HashSet without using built-in hash table libraries, we can use **hashing with separate chaining**. The idea is to distribute keys across multiple buckets using a hash function. Keys that map to the same bucket are stored in a list within that bucket.

Since the key range can be as large as \(10^6\), storing all possible keys directly would be wasteful. Instead, we use a fixed number of buckets and compute the bucket index using the modulo operation.

# Approach
- Create a fixed number of buckets (1009, a prime number to help reduce collisions).
- Use the hash function `key % buckets` to determine the bucket for a given key.
- Each bucket is a list that stores all keys hashing to that bucket.
- For `add`, insert the key only if it is not already present.
- For `remove`, delete the key if it exists.
- For `contains`, check whether the key exists in its corresponding bucket.

This approach uses **separate chaining** to handle hash collisions.

# Complexity
- Time complexity:
  - `add(key)`: **O(1)** average, **O(n)** worst case
  - `remove(key)`: **O(1)** average, **O(n)** worst case
  - `contains(key)`: **O(1)** average, **O(n)** worst case

- Space complexity:
  - **O(n + b)** where `n` is the number of stored keys and `b` is the number of buckets (1009).

"""

class MyHashSet:

    def __init__(self):
        self.buckets = 1009
        self.hashset = [[] for _ in range(self.buckets)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            keyIdx = key % self.buckets
            self.hashset[keyIdx].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            keyIdx = key % self.buckets
            self.hashset[keyIdx].remove(key)

    def contains(self, key: int) -> bool:
        keyIdx = key % self.buckets
        return key in self.hashset[keyIdx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)