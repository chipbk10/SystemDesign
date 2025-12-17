## Encoding & Decoding
- **Encoding** is to convert data from one format to another
- **Decoding** reverses the process, converting the encoded data back to its original form


## ✅ Common Encoding Types in Web Context
- **URL** Encoding (Percent-Encoding) → For query strings and form data.
- **Base64** Encoding → For binary data in text-based protocols (e.g., sending images in JSON).
- **HTML Entity** Encoding → For special characters in HTML (< → &lt;).
- **UTF-8** Encoding → For international characters.

## How Base64 Encoding works?

- Base64 characters (a..z, A..Z, 0-9,+,/) will turn binary data (like images or files) into text
- Each Base64 character represents 6 bits
- For example: given a binary data: `0x123456789ABCDEF0 (hex)`, base64 encoding will turn into `EjRWeJq83vA=`

## How URL Encoding works?

### ✅ Why Encode a URL in an HTTP Request?

When you attach a long URL as a query parameter, certain characters in the URL (like `?`, `&`, `=`, `:`) have **special meanings in HTTP**. If you don’t encode them, the server might misinterpret the request.

Example:

    GET /api/shorten?url=https://www.example.com:80?x=a&y=b

Here:

*   `?` starts the query string.
*   `&` separates parameters.
    So the server might think `y=b` is another parameter, not part of the original URL.

***

### ✅ Solution: **URL Encoding**

*   URL encoding replaces unsafe characters with **percent-encoded values**:
    *   `:` → `%3A`
    *   `/` → `%2F`
    *   `?` → `%3F`
    *   `&` → `%26`
*   So the encoded URL becomes:

<!---->

    https://www.example.com:80?x=a&y=b
    ↓
    https%3A%2F%2Fwww.example.com%3A80%3Fx%3Da%26y%3Db

Then your request is:

    GET /api/shorten?url=https%3A%2F%2Fwww.example.com%3A80%3Fx%3Da%26y%3Db

***





