I. **Hash Table**
- a hash-table (or hash-map) is a data structure that provides fast access to data using `key-value` pairs
- it's implemented using a hash function to map keys to specific positions in an underlying array.
- the goal is to achieve average-case **O(1)** time complexity for operations like insertion, deletion, and lookup

II.**Implementation**
- start with an array of a fixed size
- use a hash function (e.g., [MD5]()) to converts the key into an integer, then maps it to an array index = `hash(key) % array_size`
- if the `array[index]` is empty, store the key-value pair there (e.g., `array[index] = (key, value)`)
- if there's a collision (another pair already exists at that index),
  - either use a linked-list to contains all the paris at the same index
  - or probe for the next available slot (e.g., check at `index+1`, `index+2`, etc.)
- if the hash-table gets too full (e.g., load-factor = number-entries/array-size > 0.7),
  - then we double the array size
  - rehash all existing key-value pairs into the new array. Note that this is **O(n)**
