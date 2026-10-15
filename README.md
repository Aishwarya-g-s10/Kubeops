# KubeOps

KubeOps is an observability and AIOps platform designed to monitor application metrics and logs. When it detects abnormal behavior, it collects the relevant metrics and logs for further investigation. It can then analyze the collected data and generate a summary of the issue, including potential contributing factors and probable root causes.

DAY 1
- Created FastApi Service
- Containerized the application using docker
- Created the initial docker image 

DAY 2
- Deployed Kubeops in Kubernetes

DAY 3
- Configured liveness probe and readiness probe in the deployment
- Liveness probe checks whether the container is alive and whether it needs a restart
- Readiness probe checks whether the container or application is ready to recive traffic
- Tested readiness probe failure by configuring incorrect endpoint
- observed the pod became unready without restarting the container

DAY 4
- Configured Fastapi Instrumentator to record the application metrics
- Exposed the collectd metrics through the /metrics endpoint.