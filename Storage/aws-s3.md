## Object Storage AWS S3
- Amazon S3 is an object storage service that offers scalability, data availability (backup & restore critical data), security, analytics, AI and performance
- Price: **0,02$/1GB**
- S3 doesn't support **batching** multiple parts into a single HTTP requests.
- S3 support **parallel** uploads by sending multiple HTTP Puts concurrently (no need in any order)

## How to upload?
- to initiate, S3 returns an `upload-id`, based on that our back-end can generate URLs which allows to upload partly
- our back-end calls AWS SDK's `getSignedURL` method to generate pre-signed URLs for each part.
- a **pre-signed URL** is a temporary, secure URL (contains a AWS signature) that allows the third-party to download or upload objects without requiring them to have AWS credentials or permissions
- S3 doesn't require specifying the number of upload parts upfront
- the client can decide how many parts to split. S3 Multipart Upload requires parts **≥5MB** (except the last) and **≤5GB**, with up to **10,000 parts**
- **best practice** is:
  - use small chunks (5-10MB), ensuring the resumability
  - upload multiple parts in parallel, ensuring fast uploads
  - use pre-signed URLs to offload backend servers, and bypass the payload limit from our API Gateway (e.g., if we use AWS API Gateway, the payload limit is 10MB)
- client upload a part to a pre-signed URL together with metadata (e.g., part-number, md5 hash, AWS signature, etc.)
- S3 checks md5 hash to verify the integrity, and return an ETag
- client finishes uploading all parts, and finally sends the complete request together with all ETags
- based on ETags, S3 assembles all parts to construct the entire object. Then S3 returns 200 & the final object's ETag, which is used for later downloading
- [AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)

## How to resume?
- our back-end calls S3 ListParts api to get a list of successful uploaded parts
- note that, S3 ListParts api needs AWS credential, so the client needs to call via our back-end
- based on that list, the client knows what parts are missing
- to resume, the client just needs to upload the missing parts with pre-signed URLs
- note that, the pre-signed URLs lifetime is short (e.g., within 1 hour). In case, the pre-signed URLs expire, the client has to ask for new pre-signed URLs from S3 via our back-end
