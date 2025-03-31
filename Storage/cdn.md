I.**CDN - Content Delivery Network**
- A CDN is a network of distributed servers (`edge` nodes) spread across multiple geographic locations.
- It’s primarily used to cache content (like web pages, images, or videos) closer to users for faster delivery, but it also offers security and traffic management features, including rate limiting.
 
II.**How?**
1. **Traffic Interception**:
- When a user or client sends a request (e.g., to load a webpage or call an API), it first hits the CDN’s edge servers instead of going directly to your origin servers (your actual infrastructure).
- client -> sends request -> DNS route to CDN -> CDN points to a CDB edge server (closers to user location)
 
2. **Caching**:
- if the response is cached, and still valid, CDN will return a cached data immediately. Otherwise CDN forwards to the origin server

3. **Rate Limiting**:
- CDN might apply predefined rules to monitor and control the incoming requests rate. For example:
  - allow only 100 requests per minute per IP address, API key
  - block requests from a specific region if they exceed a threshold

III.**Types**
1. **Pull**
- CDN fetches content from your origin server based on `TTL` (Time-To-Live) we set in http headers
2. **Push**
- manually upload content to CDN providers, so it doesn’t automatically update from your origin

IV.**CDN Providers**
- Cloudflare, Akamai, Amazon CloudFront



