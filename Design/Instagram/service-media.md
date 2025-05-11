# Media Service
- is responsible to upload/download a media

## How it works?
- generates `media_id`, and stores metadata (`user_id`, `title`, `media_type`, `media_url`, `upload_time`) in key-value NoSQL (e.g., DynamoDB) that supports persistent storage.
- uploads raw media to S3 (temporary bucket) with a short lifecycle (e.g., days), or let our mobile/web app talk directly with S3
- publishes to Message Queue (e.g., Kafka) for processing 

## Media Processing Worker:
- a worker (e.g., Lambda function) picks up the task from the queue
- downloads the raw media from S3 temp-bucket
- process it (e.g., transcodes video to 720p H.264, resize image, generate thumbnails, etc.)
- uploads processed media to S3 permanent bucket (retained long-term)
- we can configure the CDN (e.g., AWS CloudFront) to automatically cache S3 objects (**@TODO**)
- updates DynamoDB with new metadata (e.g., processed_s3_url, status: "processed", etc.)

## Questions

1. **How do you upload a media?**
- we use HTTPs POST to upload for a small or medium file size
2. **How do you handle with a heavy file (> 100MB)?**
- see how to upload a big file in sub design
3. **Why is preprocessing raw media needed?**
- preprocessing ensures the media is optimized for storage, delivery, user experience, performance, and cost considerations.
- see preprocessing upload media for more details
4. **How does a full media metadata look like?**
```json
{
  "media_id": "550e8400-e29b-41d4-a716-446655440000",
  "user_id": "12345",
  "title": "Mountain Adventure",
  "media_type": "video",
  "upload_time": "2025-05-08T12:00:00Z",
  "status": "processed",
  "temp_s3_url": "s3://temp-bucket/550e8400-e29b-41d4-a716-446655440000.mp4",
  "processed_s3_url": "s3://processed-bucket/550e8400_720p.mp4",
  "thumbnail_s3_url": "s3://processed-bucket/550e8400_thumbnail.jpg",
  "etag": "d41d8cd98f00b204e9800998ecf8427e-20",
  "file_size": 52428800
}
```
5. **How does a download flow look like?**
- client requests `GET /api/media/download/{media_id}`
- our Media Service looks up the media in DynamoDB based on `media_id`
- our Media Service generates CloudFront-signed URLs dynamically for downloads, using `processed_s3_url`
- client hits CloudFront for a processed media
- CloudFront serves the cached media or fetches it from S3 if not cahced
  
7. **Does worker upload using multiple parts?**
- yes, for large files. Workers split into chunks (e.g., 5MB), and upload in parallel for reliability and performance
- no, for small files. Worker uses single-part `PutObject` for simplicity
