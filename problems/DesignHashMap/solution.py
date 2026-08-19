"""
# Intuition
The key idea is to use **hashing with separate chaining** to handle collisions.

Since multiple keys can map to the same hash bucket, each bucket stores a list of keys and their corresponding values. To efficiently locate a key within a bucket, a helper function is used to find the index of the key. This index allows us to perform insertion, update, lookup, and deletion operations.

For deletion, instead of removing an element from the middle of a list and shifting all remaining elements, we swap the target element with the last element and then pop it. This makes the actual deletion operation constant time after locating the key.

# Approach

1. Initialize a fixed number of buckets (`1009`), where each bucket stores:
   - A list of keys.
   - A corresponding list of values.

2. Use the hash function:

   ```python
   bucket = key % bucketSize
   ```

   to determine the bucket for a given key.

3. For `put(key, value)`:
   - Find whether the key already exists in the bucket.
   - If it exists, update its value.
   - Otherwise, append the key and value to their respective bucket lists.

4. For `get(key)`:
   - Find the key within its bucket.
   - Return the associated value if found; otherwise return `-1`.

5. For `remove(key)`:
   - Find the key within its bucket.
   - Swap it with the last element in both key and value lists.
   - Remove the last element using `pop()`.

# Complexity

- Time complexity:

  - `put`: **O(k)**
  - `get`: **O(k)**
  - `remove`: **O(k)**

  where `k` is the number of elements in a bucket.

  Average-case complexity is **O(1)** due to hashing and uniform distribution of keys.

- Space complexity:

  **O(n + B)**

  where:
  - `n` = number of stored key-value pairs
  - `B` = number of buckets (`1009`)

"""

class MyHashMap:

    def __init__(self):
        self.bucketSize = 1009
        self.keys = [[] for _ in range(self.bucketSize)]
        self.values = [[] for _ in range(self.bucketSize)]

    def __getKeyIndex(self, bucket, key):
        for i, k in enumerate(self.keys[bucket]):
            if k == key:
                return i
        return -1

    def put(self, key: int, value: int) -> None:
        bucket = key % self.bucketSize
        keyIdx = self.__getKeyIndex(bucket, key)

        if keyIdx == -1:
            self.keys[bucket].append(key)
            self.values[bucket].append(value)
        else:
            self.values[bucket][keyIdx] = value

    def get(self, key: int) -> int:
        bucket = key % self.bucketSize
        keyIdx = self.__getKeyIndex(bucket, key)

        if keyIdx != -1:
            return self.values[bucket][keyIdx]

        return -1

    def remove(self, key: int) -> None:
        bucket = key % self.bucketSize
        keyIdx = self.__getKeyIndex(bucket, key)

        if keyIdx != -1:
            self.keys[bucket][keyIdx], self.keys[bucket][-1] = (
                self.keys[bucket][-1],
                self.keys[bucket][keyIdx]
            )

            self.values[bucket][keyIdx], self.values[bucket][-1] = (
                self.values[bucket][-1],
                self.values[bucket][keyIdx]
            )

            self.keys[bucket].pop()
            self.values[bucket].pop()


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key, value)
# param_2 = obj.get(key)
# obj.remove(key)