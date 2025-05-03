# Question
- Let's design a photo-sharing service like Instagram, where users can upload photos to share them with other users.

# Step 1: Clarify Requirements

## Functional Requirements:
- **Upload/Download/View Photos & Videos**: Users can upload media, download them, and view them in the app.
- **Search by Titles**: Users can search photos/videos based on their titles.
- **Follow Users**: Users can follow/unfollow others to see their content.
- **News Feed**: Display a feed of top (most recent) photos/videos from followed users.

## Non-Functional Requirements:
- **High Availability**: System remains accessible even if some components fail; temporary delays in showing new photos are acceptable.
- **High Reliability**: No uploaded photo/video is ever lost.
- **News Feed Latency**: Generate news feed in ≤200ms.
- **Low Latency for Viewing Photos**: Fast photo/video loading (e.g., <100ms via CDN).

## Capacity Estimation and Constraints
- 10M [DAU]() (daily active users)
- each uploading ~2 media/day
- each viewing ~100 media/day
- average media size: 2MB (a photo), 10MB (a video)
- media uploaded from mobile/web apps
- @Todo: total space required to upload media for 1 day
- @Todo: total space required to maintain our system for 10 years

# Step 2:
- @Todo
