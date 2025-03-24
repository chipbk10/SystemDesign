I.**Read Replicas**
- is used for read-heavy apps
- master db is used only for writes
- replicas db is used for reads
- replicas is built-in tools (e.g., MySQL, PostgreSQL)

II.**Sync**
1. **Asynchronous**
- Master writes to its db and log, replicas pull and apply changes whenever they can (lag: milliseconds to seconds)
2. **Synchronous**
- Master waits for (**at least one of**) replicas to confirm the replicas have received and applied the change before confirming the write back to the app.
- No lag for read, but lag for write

III.**Communication**
- replicas communicate with master via db specific protocol (low-level sync system)
- replicas use dedicated user account on master db to access only the logs file

IV.**Master goes down**
1. **failover**:
- failover to a new master (hot standby)  or replica (leader election) that can be promoted to a new master
- failover's downtime takes from few seconds to minutes (unless fully automated)
2. **load balancing and retry**:
- add retries or circuit breakers to handle temporary slowdowns gracefully
3. **multi-master**:
- use a multi-master setup where multiple masters can accept writes
- risk of write conflicts, complex to manage
4. **fallback to read-only mode**:
- temporarily switch the app to a read-only mode where users can still browse but not modify data
- notify users of maintenance or downtime
5. **monitor and alerts**
- use monitoring tools to detect when the master is slow or down
- alert your team immediately to provide a quick solution

