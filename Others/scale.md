- when you scale up, you have to migrate data to a new server.
- the migration leads to the downtime of your service.
- for example, users expect high availability - **99,9% uptime** means **8,76 hours/year** of downtime max (0,001 * 24 * 365)
- thinking about the network speed on a decent cloud setup (e.g., 1Gbps = **125 MB/s**), and transfering **200 MB takes ~ 1.6 seconds** in theory. However, with Redis command overhead and latency, transferring together with **200 MB data might take 5-10 seconds** in practice.
