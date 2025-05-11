## Preprocessing Uploaded Media
- Preprocessing ensures the media is optimized for storage, delivery, and user experience, addressing compatibility, performance, and cost considerations.

1. **Optimization for delivery**: **@TODO**
- **Video**:
  - raw videos (e.g., 100MB mp4 from a mobile device) may be in high-resolution formats (e.g., 4K, 60fps) with large file sizes, which are slow to stream and consume significant bandwidth
  - preprocessing involves transcoding to create multiple resolutions (e.g., 1080p, 720p, 480p) and formats (e.g., HLS for adaptive streaming), ensuring smooth playback across devices and network condition

- **Images**:
  -  raw images (e.g., 10MB jpegs) may need resizing (e.g., thumbnails, medium, full-size) and compression (e.g., WebP format) to reduce load times and storage costs while maintaining quality
    
2. **Compatibility**
- different devices and browsers support varying media formats. For example, iOS prefer H.264 mp4, while Android may support VP9/WebM. Preprocessing converts raw media into widely compatible formats
   
3. **User Experience**
- preprocessed media enables adaptive bitrate streaming, where the video player switches resolutions (e.g., 720p to 480p) based on network speed, reducing buffering
- thumbnails and previews (e.g., for video timelines or image galleries) enhance navigation and engagement

4. **Cost Efficiency**
- raw media consumes more storage and bandwidth. Preprocessing reduce file sizes (e.g., compressing a 100MB to 50MB) and optimizes delivery via CDN, lowering S3 and data transfer costs
  
5. **Metadata extraction**
- preprocessing extracts metadata (e.g., video duration, resolution, audio channels) to store in DynamoDB, enabling features like duration display or format validation
