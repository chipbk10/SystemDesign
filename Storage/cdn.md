I.**CDN - Content Delivery Network**
- is a system of distributed servers that deliver web content—like css, images, videos, stylesheets, or scripts—to users based on their geographic location
- it speeds up content delivery by caching it on edge servers closer to the user, reducing latency and improving performance.
- CDNs also help handle traffic spikes and reduce the load on your main server.

II.**How?**
- register your static content with a CDN provider and then update your HTML or JavaScript code to use the CDN-provided links

II.**Types**
1. Pull
- CDN fetches content from your origin server based on `TTL` (Time-To-Live) we set in http headers
2. Push
- manually upload content to CDN providers, so it doesn’t automatically update from your origin

III.**CDN Providers**
- Cloudflare, Akamai, Amazon CloudFront



