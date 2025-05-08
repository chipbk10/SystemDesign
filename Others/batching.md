# Batching
- batching refers to combine mulitple parts (e.g., mulitple api calls, mulitple data types) into a single http request
- to reduce the number of HTTP requests, minimizing overhead like connection setup and latency

## batch API calls
- [batching multiple API calls](https://learn.microsoft.com/en-us/graph/json-batching?tabs=http) in a JSON request body 
- we can specify the requests in the batch to be executed in a specified order or in parallel

## batch multi-parts
- batching involves combinding multiple parts using `multipart/form-data` into a single HTTP request
- the request body is divided into multiple parts (that might represent different data types), each separated by a boundary string
- each part contains headers (e.g., `Content-Disposition`, `Content-Type`), and the actual data (binary data, json)
```
POST /upload HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="username"

john_doe
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="profile_picture"; filename="profile.jpg"
Content-Type: image/jpeg

[Binary data of the JPEG file]
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="metadata"
Content-Type: application/json

{"age": 30, "location": "New York"}
------WebKitFormBoundary7MA4YWxkTrZu0gW--j
```
- batching increases request **size** (e.g., 20MB for 4 parts), risking **timeouts** or **payload limits** (e.g., API Gateway’s 10MB limit)


