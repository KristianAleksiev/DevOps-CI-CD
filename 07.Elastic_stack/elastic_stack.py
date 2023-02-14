"""
1. Elastic stack (ELK stack)
- Elastic search - Searching, analyzing and storing of data, Distributed analytics engine,
Designed for horizontal scalability

- Logstash - Server-side data collection and processing pipeline
- Kibana - Data visualization and Elastic stack navigation (~Grafana)

2. Beats
Single-purpose data shipper
No processing of data, only gather and send

- Heartbeat - Monitor services for availability with active probin
- Metricbeat - Colelct metrics from systems and services
- Filebeat - Forward logs and files
- Auditbeat - Audits the activities of users and processes on the systems

3. Elastic stack and Docker
- Docker monitoring as well as its containers
- as docker-compose clients
"""