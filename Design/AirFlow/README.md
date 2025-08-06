# Question
- Let's design a scalable distributed Job Scheduler like AirFlow

# Clarify Requirements

## Functional Requirements
- users can submit a job/task to run based on a particular schedule (recurring/single time, after some dependent jobs are done, etc)
- users can see the status of a job (success, failure with error message, cancelled, etc.)
- users can cancel a job
- nice to have
  - users can manually trigger a job execution

## Non-Functional Requirements
- **Scalability**: The system can handle 10 billions jobs a day (10K jobs per second)
- **Latency**: The system ensures a low latency (1-2 seconds delay) job schedule. It means a job might be executed 1-2 seconds later than expected. 
- **Security**:
  - jobs should not harm our system
  - one job execution should not impact on other running jobs    
- Availability: high
- Reliability:
  - even if the system is down, the jobs received should not be lost. System should be durable
  - each job should run at least once
  - we can retry if a job failed to be executed
- Consistency: eventual consistency (means we might see some delay 1-2 seconds of the jobs' status)

