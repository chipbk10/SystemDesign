# Question
- Design a scalable online judge, like Leetcode, HackerRank

# Clarify Requirements

## Functional Requirements
- users can submit code, execute it against test cases, and receive results in real-time
- users can submit code in contest and see the leaderboard
  
## Non-Functional Requirements
- availability:
  - high availability: 99.9% uptime (e.g., 8.76 hours of downtime per year)
- scalability:
  - the system can handle up to 10K concurrent users submitting code concurrently during peak times.
  - each submission requires execution of 1K test cases on average
  - the system can support 20 languages
- low latency:
  - the system should return the result within a few second for every submission
- security:
  - **Code Execution Safety**: submitted code cannot harm the system (e.g., prevent malicious code from accessing system resource, files, or networks)
  - **User Data Isolation**: one user's submission or results cannot interfere with or access another user's data (e.g., test case outputs, or other user's code) 
