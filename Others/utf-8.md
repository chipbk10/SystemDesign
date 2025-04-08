I.**How UTF-8 encoding works**
- **UTF-8** is a variable-length encoding, meaning characters can take 1, 2, 3 or 4 bytes.
  
1.Byte Sequence (**ASCII**, U+0000 to U+007F):
- Starts with **0xxxxxxx** (0 followed by 7 bits).
- Represents the 128 ASCII characters (e.g., "A" = 01000001).
- Range: 0 to 127 in decimal.

2.Byte Sequence (e.g., **Latin accents**, U+0080 to U+07FF):
- Starts with **110xxxxx** (first byte) followed by **10xxxxxx** (second byte).
- Uses 11 bits total for the code point (5 from the first byte, 6 from the second).
- Example: "é" (U+00E9) = 11000011 10101001.

3-Byte Sequence (e.g., **Asian characters**, U+0800 to U+FFFF):
- Starts with **1110xxxx** (first byte) followed by **10xxxxxx** (two continuation bytes).
- Uses 16 bits total.
- Example: "汉" (U+6C49) = 11100110 10110001 10001001.

4-Byte Sequence (e.g., **emojis**, U+10000 to U+10FFFF):
- Starts with **11110xxx** (first byte) followed by **10xxxxxx** (three continuation bytes).
- Uses 21 bits total.
- Example: "" (U+1F60A) = 11110000 10011111 10011000 10001010.

