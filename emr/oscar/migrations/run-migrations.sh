#!/bin/sh
set -e

HOST=oscar-db-0.oscar-db.oscar-emr.svc.cluster.local

mysql -h "$HOST" -u oscar -poscarpw oscar < /migrations/oscarinit.sql
mysql -h "$HOST" -u oscar -poscarpw oscar < /migrations/oscardata.sql
mysql -h "$HOST" -u oscar -poscarpw oscar < /migrations/initcaisi.sql &&
mysql -h "$HOST" -u oscar -poscarpw oscar < /migrations/initcaisi_data.sql &&
mysql -h "$HOST" -u oscar -poscarpw oscar < /migrations/patch19.sql
