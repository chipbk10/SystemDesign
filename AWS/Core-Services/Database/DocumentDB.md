- Amazon DocumentDB is not serverless. It runs on provisioned instances (similar to RDS), so you need to choose instance types and manage capacity.
- **DocumentDB** = Managed **MongoDB**-compatible **document** database
- document here refers to **JSON-like data structures**
```json
{
  "customer_id": 123,
  "name": "Alice",
  "orders": [
    {"id": 1, "item": "Laptop"},
    {"id": 2, "item": "Mouse"}
  ]
}
```
- compare with DynamoDB:
  - DynamoDB supports nested attributes (maps and lists), so you can store complex data similar to JSON.
  - however, DocumentDB supports document queries @Todo
