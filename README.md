Project: Data Pipelines with Airflow
-------------------------------

Introduction:
----------------------
A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow,Our goal is to build high-grade data pipelines that are dynamic and built from reusable tasks, can be monitored and allow easy backfills. We also want to improve data quality by running tests against the dataset after the ETL steps are complete in order to catch any discrepancies.

The source data is in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source data are CSV logs containing user activity in the application and JSON metadata about the songs the users listen to.

Datasets:
---------------
Log data: s3://udacity-dend/log_data
Song data: s3://udacity-dend/song_data

Schema for project:
-------------------------

![image](https://user-images.githubusercontent.com/52973147/100525293-948a9200-31d0-11eb-9f14-57b78d5aa3ae.png)

DAG :
--------------------------
![image](https://user-images.githubusercontent.com/52973147/107270297-d13df980-6a5b-11eb-8a3a-f1bf5f9a6893.png)
