- required to upload a big file (e.g., video ~ 10MB)
- our service
  - generate a object-id, and store metadata in a NoSQL database (e.g., DynamoDB). Why NoSQL? scales horizontally for high write/read throughput (upload & read file)
  - upload raw data to a NoSQL database (e.g., S3 temporary bucket)
  - dsfdsfs
 
# Questions

1. **Is uploading a big file via standard HTTPS POST synchronous?**
- Yes, a standard HTTPS POST for uploading a file is a synchronous request. The client sends the file data, and the server processes it, keeping the connection open until the upload completes or fails, then returns a response.

2. **How long does a standard HTTPS POST take to respond?**
- The response time depends on file size, network speed, and server processing. For a 10MB file on a typical 10Mbps upload speed, it takes ~8 seconds (10MB × 8 bits/byte ÷ 10Mbps) plus ~100-200ms for server acknowledgment and network latency, totaling ~8.2 seconds. This assumes no congestion or throttling.

3. **What if the media file is 1GB?**
- For a 1GB file on a 10Mbps upload speed, the upload takes ~800 seconds (1GB × 8 bits/byte ÷ 10Mbps) or ~13.3 minutes, plus ~100-200ms for server response, totaling ~800.2 seconds. On faster networks (e.g., 100Mbps), it drops to ~80 seconds. However, large files like 1GB are prone to failures (e.g., network drops), making multipart uploads (splitting into chunks) preferable, though still synchronous per chunk.

4. **If you use standard HTTPS POST to upload a big file (e.g., a video ~10MB), how do you show the uploading progress from the front-end app?**
- The front-end app uses the `S3 Multipart Upload API`, which splits the 10MB video into smaller chunks (e.g., 5MB each). The app tracks progress by monitoring the completion of each chunk’s HTTPS POST request. Most mobile frameworks (e.g., iOS’s URLSession, Android’s OkHttp) provide callbacks for upload progress, calculating the percentage (e.g., bytes sent ÷ total bytes). The app updates a progress bar UI in real-time based on these callbacks.

5. **You store metadata in DynamoDB, and in the meantime, use a message queue to asynchronously upload multiple parts of the big file to S3. You don’t wait until the raw data is completely uploaded to S3, you immediately return a success response to the client?**
- No, I don’t return a success response immediately. The Media Service first stores metadata in DynamoDB and synchronously uploads all parts of the file to a temporary S3 bucket using S3 Multipart Upload. Once all parts are uploaded to S3 (confirmed by S3’s response), the service returns a success response to the client. Only then does it publish a message to the Message Queue (e.g., Kafka) for asynchronous processing (e.g., resizing, transcoding). This ensures the raw data is safely stored before acknowledging success, maintaining reliability.

6.**After a threshold (3 failed attempts), you will return a failure response, and delete the metadata from DynamoDB?**
- If the Message Queue enqueuing fails after 3 retries (e.g., for media processing), the Media Service moves the message to a dead-letter queue (DLQ) and returns a failure response to the client (e.g., “Processing failed, please retry”). However, I don’t delete the metadata from DynamoDB or the raw data from the temporary S3 bucket. Keeping them allows manual recovery or debugging (e.g., re-enqueuing the processing task). The metadata is marked with a status (e.g., “failed”) to indicate the issue, ensuring no data loss.

7.**For uploading a media, do you use long-polling HTTPS? How do you upload a big video (~10MB) to S3? Do you truncate the file into small parts?**
- Long-polling HTTPS: No, I use standard HTTPS POST for uploads to keep it simple and reliable. Long-polling is unnecessary as uploads are synchronous up to the temporary S3 bucket.
- Uploading a 10MB video: Use S3 Multipart Upload. The client splits the video into smaller parts (e.g., 5MB chunks) and uploads them in parallel to S3. This improves speed, handles network interruptions, and allows resuming failed uploads. Once all parts are uploaded, S3 assembles them into the final file.

8. **Why do we need an S3 temporary bucket to store raw media data?**
- A temporary S3 bucket holds raw, unprocessed media (photos/videos) during upload to decouple the upload from processing. This ensures fast user response (upload acknowledged quickly) while allowing asynchronous processing (e.g., resizing, transcoding) without tying up client connections or risking data loss if processing fails.








