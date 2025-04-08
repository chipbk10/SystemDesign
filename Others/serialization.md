- `Serialization` is the process of coverting a complex data structure (like objects, arrays, or graphs) into a flat, linear and **portalbe** format (e.g., a byte stream or text) that can be stored, transmitted, or reconstructed later.
- `Serialization` is about **structure** - preserving an object's state and relationships
- For example, we serialize the following object into a json string
  - ```
    class Person {
      String name;
      int age
    }
    ```
  - json: `{ "name": "John", "age": 30 }`

- `Encoding` is the process of converting data from one form to another, typically make it compatible with a specific system or protocol
- `Encoding` is about **representation** - how data is expressed in bits or characters
- For example,
  - after serializing (convert to json), we encode (use utf-8 encoding) to turn the string into bytes, and send to another computer
  - the other computer will `decode` (using utf-8 decoding) to turn the bytes into json string
  - the other computer `deserialize` json string into `Person` object
