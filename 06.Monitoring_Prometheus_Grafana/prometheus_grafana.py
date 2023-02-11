"""
1. Prometheus
- Architecture
Toolkit for monitoring and alerting
Purpose - Collection and preservation of data
Collected data metrics are stored as time series data
Pull model data collection over HTTP
Intermediary gateway for pushing data

- Config
Command-line flags and a Configuration files (yaml format)
Using containers
Using config management systems - Ansible, Chef, Puppet and Salt

- Information processing and PromQL
Metric types:
Counter - Monotonically increasing counter
Gauge - single numerical value that can go up and down (e.g. active sessions)
Histogram - Sample observations (durations, sizes)
Summary - Total count of observations and a sum of all observed values

- Prometheus jobs(apps), data scraping
- Relabeling - Target / Metric
2. Grafana
Complete observability stack
Monitor and analyze metrics, logs
Supports SQLite, MySQL and PostgreSQL

Administration files -> defaults.ini, grafana.ini, custom.ini

Grafana panels - Building blocks of dashboards - Connected to a datasource
- Dashboarding
"""