# Requirements

## Functional Requirements
- users can upload a big file (e.g., a video ~ 100MB or 1GB), together with metadata (e.g., filename, file_type, author_name, created_at, etc.)
- users can resume the upload after closing the browser, or terminating mobile app
- users can see the upload progress
- users can download a file

## Non-Functional Requirements:
- reduce the upload time as much as possible
- ensure the integrity of the uploaded file 
- scalability, serving millions of uploads concurrently

# High-Level Design

- web/mobile app -> API GateWay -> Our API -> Storage
- we will use NoSQL key-value type (e.g., AWS DynamoDB) to store metadata
  - DynamoDB supports persistent storage (disked-based)
  - DynamoDB is fast, and we don't need complex queries with relationship like SQL
  - file_id (Partition Key), value: json {filename, file_type, file_size, author_name, upload_status, created_at, upload_id, path_url, eTag}
- we will use Object Storage (e.g., AWS S3) to store binary data of the file
  - it's not a good practice to store a big file (as BLOB) in SQL database (not natively support, slow on query)
  - AWS S3 supports multiple parts upload
  - AWS S3 supports resume functionality
  - AWS S3 supports millions of upload/download at a time
  - AWS S3 supports pre-signed URLs that alows our web/mobile app uploads a big file to S3 directly without AWS credential. This will decrease the load on our server.
- we will split big file in chunks, and upload chunks in parallels
- if something wrong (e.g., network disrupted, app terminated), we can resume by uploading the failed chunks
- we store the upload status in metadata like: uploading, uploaded, failed

# Flows
- web/mobile app calls `/api/upload/init` together with metadata in request body
  - our back-end stores metadata in DynamoDB, and the status is `uploading`
  - our back-end calls S3 to initiate an upload process
  - S3 returns `upload_id`
  - our back-end generates URLs and calls S3 to sign
  - our back-end returns upload_id, pre-signed URLs, so that our web/mobile app can upload directly to S3
- web/mobile app split big file in chunks, and upload in parallel
  - once each part is uploaded, S3 will return an ETag
  - once all parts are uploaded, our web/mobile app will send all ETags to S3 (via our back-end as it needs AWS credential)
  - based on these ETags, S3 assembles and constructs a total object, and returns a ETag, temp_s3_url, Bucket, Key, etc.
  - our back-end will store **temp_s3_url** & ETag in metadata
- web/mobile app calls `/api/download/file_id` to download a file
  - based on `temp_s3_url`, our back-end asks S3 to generate a pre-signed URL
  - with this pre-signed URL, our web/mobile app download a file from S3 directly
- to resume uploading, our web/mobile app just needs to upload failed parts by using the pre-signed URLs
  - if pre-signed URLs expired, our web/mobile app will call `/api/upload/refresh_urls` to our back-end to re-generate new pre-signed URLs
- consider the number of parallel uploads based on the fact that during upload, actually we store the chunks in our front-end memory










