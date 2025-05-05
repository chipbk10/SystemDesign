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

6. **After a threshold (3 failed attempts), you will return a failure response, and delete the metadata from DynamoDB?**
- If the Message Queue enqueuing fails after 3 retries (e.g., for media processing), the Media Service moves the message to a dead-letter queue (DLQ) and returns a failure response to the client (e.g., “Processing failed, please retry”). However, I don’t delete the metadata from DynamoDB or the raw data from the temporary S3 bucket. Keeping them allows manual recovery or debugging (e.g., re-enqueuing the processing task). The metadata is marked with a status (e.g., “failed”) to indicate the issue, ensuring no data loss.

7. **For uploading a media, do you use long-polling HTTPS? How do you upload a big video (~10MB) to S3? Do you truncate the file into small parts?**
- Long-polling HTTPS: No, I use standard HTTPS POST for uploads to keep it simple and reliable. Long-polling is unnecessary as uploads are synchronous up to the temporary S3 bucket.
- Uploading a 10MB video: Use S3 Multipart Upload. The client splits the video into smaller parts (e.g., 5MB chunks) and uploads them in parallel to S3. This improves speed, handles network interruptions, and allows resuming failed uploads. Once all parts are uploaded, S3 assembles them into the final file.

8. **Why do we need an S3 temporary bucket to store raw media data?**
- A temporary S3 bucket holds raw, unprocessed media (photos/videos) during upload to decouple the upload from processing. This ensures fast user response (upload acknowledged quickly) while allowing asynchronous processing (e.g., resizing, transcoding) without tying up client connections or risking data loss if processing fails.

9. **If you use only the standard https post, so how you can get updated for the uploading progress?**
- To show upload progress for a big file using a standard HTTPS POST, the front-end app relies on client-side mechanisms provided by modern web or mobile frameworks, as the standard HTTPS POST itself doesn’t inherently send progress updates from the server. 
- As the client sends the file data in a standard HTTPS POST, these APIs track the number of bytes sent versus the total file size.
- The app calculates the percentage (bytes sent ÷ total bytes) and updates the UI (e.g., progress bar) in real-time
- If the connection drops, the entire POST fails, and no progress is saved (unlike multipart uploads).

10. **Do Instagram and Facebook apps use standard HTTPS POST for uploading?**
- Instagram and Facebook apps likely do not rely solely on a single standard HTTPS POST for uploading media (e.g., photos, videos). Instead, they use more robust methods like multipart uploads or chunked uploads over HTTPS, especially for larger files such as videos. These methods involve splitting files into smaller chunks and sending them in multiple requests, which is more efficient and resilient than a single POST. For smaller files (e.g., low-resolution photos), a standard HTTPS POST might be used due to simplicity, but for larger or high-quality media, chunked or multipart uploads are standard in modern apps to handle network variability and improve performance

11. **What happens if the connection drops?**
- If the connection drops during an upload, the upload process typically fails at the point of interruption. For a standard HTTPS POST, the entire upload would fail, and the app would display an error (e.g., “Upload Failed” or “Story Not Uploading”). For chunked/multipart uploads, only the unsent chunks are affected, and the server retains successfully uploaded chunks. Instagram and Facebook apps often show errors like “Upload Failed” or “Stuck on Sending” when a connection drops, as reported by users. The apps may retry the upload automatically if the network reconnects, but this depends on the app’s retry logic and network conditions

12. **Do they (Instagram or Facebook) have a feature to resume previous uploads?**
- There is no explicit, user-facing “resume upload” feature documented in Instagram or Facebook apps, unlike some cloud storage services (e.g., Google Cloud Storage, Dropbox). If a connection drops, the apps may attempt to retry the upload automatically in the background, leveraging chunked uploads to avoid restarting from scratch, but this is not exposed as a user-controlled feature. If retries fail, users typically see an error and must manually restart the upload. User reports indicate that uploads often fail completely on unstable connections, requiring a fresh attempt, suggesting limited or no resume functionality for end users. For example, users have reported needing to re-upload after switching networks or restarting the app









