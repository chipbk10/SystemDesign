***

### **What is a Bloom Filter?**

A Bloom filter is a **space-efficient, probabilistic data structure** used to test whether an element is **possibly in a set** or **definitely not in the set**.

*   It can **never give false negatives** (if it says “not present,” the element is truly absent).
*   It can give **false positives** (it might say “present” when the element isn’t actually there).

***

### **How it works**

1.  **Initialize a bit array** of size `m` (all bits = 0).
2.  Choose `k` independent hash functions.
3.  **Insert an element**:
    *   Compute `k` hashes of the element.
    *   Set the corresponding `k` positions in the bit array to `1`.
4.  **Check membership**:
    *   Compute the same `k` hashes.
    *   If **all `k` positions are 1**, the element **might be present**.
    *   If **any position is 0**, the element is **definitely not present**.

***

### **Example**

*   Bit array: `[0,0,0,0,0,0,0,0,0,0]`
*   Insert `"alice"`:
    *   Hash1 → index 2, Hash2 → index 5, Hash3 → index 8 → set those bits to 1.
*   Check `"bob"`:
    *   Hashes → indices 1, 4, 7 → if any is 0 → bob is definitely not present.

***

### **Why useful for login pre-check**

*   If Bloom filter says **“not present”**, you can reject immediately without hitting the DB.
*   If it says **“might be present”**, you still check the DB.
*   Saves DB hits for invalid usernames with minimal memory.
*   **Cons**: you have to set up Bloom Filter from the beginning

***
or  
✅ **Give you a short code snippet** (e.g., Python) to implement a Bloom filter?
