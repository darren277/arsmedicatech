#!/bin/sh
set -e

HOST=oscar-db-0.oscar-db.oscar-emr.svc.cluster.local
RETRIES=60

echo "Waiting for database pod ($HOST) ..."

getent hosts "$HOST" || echo "❌ getent failed to resolve $HOST"

for i in $(seq 1 $RETRIES); do
    if getent hosts "$HOST" >/dev/null; then
        echo "[$i/$RETRIES] ✅ DNS resolved, checking MySQL ..."
        if mysqladmin ping -h "$HOST" -u oscar -poscarpw --silent; then
            echo "✅ MySQL is up. Proceeding with migrations..."
            exec ./run-migrations.sh  # Replace with your actual script
        else
            echo "[$i/$RETRIES] ❌ MySQL not ready yet, sleeping 5s"
        fi
    else
        echo "[$i/$RETRIES] ❌ getent failed to resolve $HOST, sleeping 5s"
    fi
    sleep 5
done

echo "❌ Timed out waiting for MySQL"
exit 1
