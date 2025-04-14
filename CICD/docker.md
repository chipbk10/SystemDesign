I. **Questions**
- why an app developed and **containerized using Docker on a Mac (running macOS) can seamlessly run on a remote Linux server**:
  - docker Desktop on a Mac runs a docker based on a lightweight Linux VM
  - when we build a docker container on Mac, we're actually building it for a Linux environment inside this VM, not for macOS
 
- why an app developed and **containerized using Docker on a Mac (running macOS) can seamlessly run on a remote Windows server**:
  - docker on Mac uses a Linux VM
  - windows server supports Linux containers

- so, docker containers are strictly limited to Linux?
  - not exactly, but Linux containers are the most common and default type because Docker was originally built around Linux kernel features.
  - however, docker also supports Windows containers

II.**Dockerfile**
- **base image**: defines the [user space]() OS
- **dependencies**: install libraries or runtimes (e.g., `RUN apt-get install -y libssl3`, `RUN pip install flask`)
- **app code**: copies your application (e.g., `COPY ./app`)
- **runtime config**: sets environment variables, ports, or entrypoints (e.g., `EXPOSE 8080`, `CMD ["dotnet", "MyApp.dll"]`)
- **architecture**: we can specify the platform (e.g., linux/amd64), this is about CPU, not kernel


III.**How docker works?**
- @Todo
