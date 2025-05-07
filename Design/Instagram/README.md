# Question
- Let's design a photo-sharing service like Instagram

# Clarify Requirements

## Functional Requirements
- Users can share a media (photo or video) and other meta data (e.g., title, description, etc)
- Users can follow/unfollow others
- Users can search a photo or a video based on their titles
- Users can see the news feed that displays the most recent posts from the followed users

## Non-Functional Requirements
- **High Availability**: system remains accessible even if some components fail. Temporary delays in showing new posts are acceptable
- **High Reliability**: no uploaded post (including photo/video) is ever lost
- **News Feed Latency**: should generate news feed in <= 200ms
- **Low Latency for viewing media**: fast photo/video loading (e.g., < 100ms via CDN)
