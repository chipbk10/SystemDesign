I.**Universally Unique Identifier - UUID?**
- a random 128 bits, typically represented as a 36-character string in hexadecimal format. It means each character is represented by 4 bits (2^4 possibilities: 0-9, a-f). `128 = 32 * 4`, in which 32 characters, 4 hyphen (**is not represented at all**)
- split into five groups by hyphens in format: `8-4-4-4-12` (e.g., `550e8400-e29b-41d4-a716-446655440000`)
- very **low collision**

II.**UUID types**
1.**Version 1**
- contains timestamp, MAC address
- pros: sortable
- cons: expose MAC address, and generated time
2.**Version 2** (less common)
- Similar to V1 but includes a user/group ID 
3.**Version 3**
- Name-based (MD5 hash of a namespace + name)
4.**Version 4** (most common today)
- Randomly generated except for version bits (@Todo)
5.**Version 5**
- Name-based (SHA-1 hash of a namespace + name). Like V3 but more secure

III.**Application**
- is used to assign **unique identifiers** without requiring a central authority to coordinate or register them.
- for example, uuid is used for database `primary keys`, `transaction-id`, `file-id`, `session-id`, `device-id`
- works offline or in distributed environments
- cons: larger than `sequential ids`, not human-readable, not sortable (except V1 - but exposes system info)
