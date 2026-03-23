# Obfuscation
- In software engineering, obfuscation is the intentional practice of making source or machine code difficult for humans to understand while maintaining its original functionality. It is primarily used to protect intellectual property, prevent reverse engineering, and enhance security.

## Common Techniques & Examples

### Identifier Renaming
- Replacing meaningful names with nonsensical labels.
- Original: `int calculateTotal(int price, int tax)`
- Obfuscated: `int a(int b, int c)`
- Use Case: Common in Android `(ProGuard)` and `JavaScript` (UglifyJS) to hide business logic.
