I.**Unicode Transformation Format - UTF**:
- unicode itself is a standard that assigns a unique number (called a **code point**) to every character

1. **UTF-8**
- uses 1 to 4 bytes per character, depending on the **code point**. See [utf-8]() for more details
- most widely used encoding because it's efficient, backward-compatible with ASCII
- is the standard for html, json, os (linux, mac - but windows uses utf-16 internally)
  
3. **UTF-16**
- uses 2 or 4 bytes per character
  
5. **UTF-32**
- uses 4 bytes for every character
- simplicity: easy to calculate the string length or access characters by index
- wasteful resources
