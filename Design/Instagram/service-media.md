# Media Service
- is responsible to upload a media

## Storage
- we store media meta data in key-value NoSQL (e.g., DynamoDB) that supports persistent storage (disked-based)
  - **key**: `media_id`
  - **value**: is a JSON object containing all relevant metadata info (e.g., `user_id`, `title`, `media_type`, `media_url`, `upload_time`)

## How it works?
- we use 


## Questions

1. **How do you upload a media?**
- we use HTTPs POST to upload for a small or medium file size
3. **How do you handle with a heavy file (> 100MB)?**
- see how to upload a big file in sub design
- we can upload directly from mobile/web app to S3 to avoid the loads on Media Service
  - mobile/web app sends `/api/media/upload/init` to Media Service
  - Media Service calls `S3` to start multiple upload


