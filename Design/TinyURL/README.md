# Question
- Let's design a scalable url shortening service like TinyURL

# Clarify Requirements

## Functional Requirements
- Given a long url, we return a shorten version
- Open a shorten url, we redirect to the long url

## Non-Functional Requirements
- **Availability**:
- **Reliability**:
- **Latency**:
- **Scalability**:
- **Security**:
- **Offline Support**:

# Challenges

## Safe Transmision
- to attach a long url together with request, we have to **encode** it (replacing special characters like :// . ?)

## Uniqueness & Consistency
- Two URLs that look different but mean the same thing (e.g., **http://example.com** vs **http://example.com:80** vs **http://example.com/**) should map to the same **consistent** form.
- We solve this problem by **normalizing** urls
- This prevents duplicate entries and ensures you don’t generate multiple short codes for the same resource.

## Collision Risk
- decision on how long is a random code?
- For example, we generate a randome code of **6 characters** from a set of **base62** characters [a..z, A..Z, 0..9]
  - in total, we have 62^6 ~ **56.8 billion**
  - the probability of generating the same one is small

# Code Generation
- on the fly vs pre-generation

## pre-generation
- Pros:
  - zero collision risk: never generate duplicates
  - fast allocation: just pop a code from the pool when needed
- Cons:
  - Storage overhead: You need to store millions or billions of unused code upfront
  - Complexity: you need a mechanism to mark codes as `used` and handle concurrently safely
  - Scalability: if you run out of pre-generated codes, you must generate more (and ensure uniqueness)

## on the fly
- Most sytems (Bitly, TinyURL) generate codes on the fly because:
  - generating on demand + checking for duplicates is simpler and scales well
  - or **Sequential ID approach** we can base62 encoding of an incrementing ID, you don't need randomness or collision checks at all
    - for example: ID = 1 -> a, ID = 62 -> 10, ID = 238327 -> zzz
    - however, it's easy to guess. Guessing is possible but not **catastrophic** (links are **public** anyway).
    - We can mitigate predictability. Instead of pure sequential IDs, use:
      - **Snowflake IDs** (time + machine + sequence → looks random) - 64 bits ~ 11 characters (base64 encoding)
      - Or **shuffle the ID space** (e.g., apply a reversible hash like XOR with a secret key before encoding).


# Database
- NoSQL key-value (like DynamoDB) vs SQL with indexing for fast look-up (like MySQL)

