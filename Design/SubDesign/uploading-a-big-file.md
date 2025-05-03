- required to upload a big file (e.g., video ~ 10MB)
- our service
  - generate a object-id, and store metadata in a NoSQL database (e.g., DynamoDB). Why NoSQL? scales horizontally for high write/read throughput (upload & read file)
  - upload raw data to a NoSQL database (e.g., S3 temporary bucket)
  - dsfdsfs
 
# Questions

1. Is uploading a big file via standard HTTPS POST synchronous?
- Yes, a standard HTTPS POST for uploading a file is a synchronous request. The client sends the file data, and the server processes it, keeping the connection open until the upload completes or fails, then returns a response.

2. How long does a standard HTTPS POST take to respond?
- The response time depends on file size, network speed, and server processing. For a 10MB file on a typical 10Mbps upload speed, it takes ~8 seconds (10MB × 8 bits/byte ÷ 10Mbps) plus ~100-200ms for server acknowledgment and network latency, totaling ~8.2 seconds. This assumes no congestion or throttling.

3. What if the media file is 1GB?
- For a 1GB file on a 10Mbps upload speed, the upload takes ~800 seconds (1GB × 8 bits/byte ÷ 10Mbps) or ~13.3 minutes, plus ~100-200ms for server response, totaling ~800.2 seconds. On faster networks (e.g., 100Mbps), it drops to ~80 seconds. However, large files like 1GB are prone to failures (e.g., network drops), making multipart uploads (splitting into chunks) preferable, though still synchronous per chunk.

4. If you use standard HTTPS POST to upload a big file (e.g., a video ~10MB), how do you show the uploading progress from the front-end app?
- The front-end app uses the `S3 Multipart Upload API`, which splits the 10MB video into smaller chunks (e.g., 5MB each). The app tracks progress by monitoring the completion of each chunk’s HTTPS POST request. Most mobile frameworks (e.g., iOS’s URLSession, Android’s OkHttp) provide callbacks for upload progress, calculating the percentage (e.g., bytes sent ÷ total bytes). The app updates a progress bar UI in real-time based on these callbacks.

5. 

