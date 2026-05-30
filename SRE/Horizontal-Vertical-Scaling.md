Handling website traffic peaks:

## 🚀 Scaling Options

* Horizontal Scaling: Adding more server instances. The load balancer automatically distributes traffic to the new instances.
* Vertical Scaling: Upgrading a single server by adding more CPU, memory (RAM), or storage.

## 🔄 Reboot Requirements for Vertical Scaling

* Storage (Hard Disk): No restart required on modern cloud providers. You expand the disk size online and resize the file system via the OS.
* CPU and Memory (RAM): Restart is usually required. The cloud provider typically shuts down the VM to allocate more hardware resources.

## 💡 Core Recommendation

* Horizontal scaling is preferred for sudden traffic peaks because it handles spikes with zero downtime.

