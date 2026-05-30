A canary deployment is a software release strategy where a new version of an application is gradually rolled out to a small subset of infrastructure or users before being deployed to the entire user base. This approach isolates potential bugs or performance issues to a tiny fraction of live traffic, minimizing the "blast radius" if something goes wrong.
The name originates from the historical practice of coal miners bringing live canaries into mines; if toxic gases leaked, the bird would show distress first, giving miners an early warning to escape. In software engineering, the small group of users or servers acts as that early warning system.
------------------------------
## How It Works: Step-by-Step

[ All User Traffic ]
         |
         v
  [ Load Balancer ]
    /          \
   v (95%)      v (5%)
[Version 1.0] [Version 2.0 (Canary)]
 (Current)       (New Feature)


   1. Phase 1: Split Traffic – You route a tiny percentage of live traffic (e.g., 5%) to the new version (v2.0), while the remaining 95% stays on the stable current version (v1.0).
   2. Phase 2: Monitor Metrics – DevOps and SRE teams track key indicators on the canary servers. They look closely at error rates, memory usage, CPU consumption, and latency.
   3. Phase 3: Roll out or Roll back
   * If a bug triggers: The traffic is immediately rerouted 100% back to v1.0. Only the 5% of users experienced the issue.
      * If performance is clean: Traffic to v2.0 is incrementally ramped up (e.g., 25% $\rightarrow$ 50% $\rightarrow$ 100%) until the entire application is upgraded.
   
------------------------------
## Real-World Example: Streaming App Update
Imagine an online video streaming service like Netflix or YouTube updating its video recommendation algorithm.

* The Setup: The service runs on 100 cloud server instances handling millions of active viewers.
* The Canary: Instead of pushing the new code to all 100 servers instantly, the engineering team deploys the new update to just 2 servers (2% of the fleet).
* The Test: The global [load balancer](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary) routes random incoming user traffic so that 2% of viewers land on the new version. These users see a slightly tweaked homepage with new recommendations, while the other 98% see the old layout.
* The Analysis: The backend automated systems notice that the 2 canary servers are experiencing a sudden spike in crash loops or taking twice as long to load videos.
* The Resolution: The automated pipeline flags the failure, stops the deployment, and flips the load balancer rule back to 0% for the new version. The vast majority of the global audience never experienced a single second of downtime or lag.
