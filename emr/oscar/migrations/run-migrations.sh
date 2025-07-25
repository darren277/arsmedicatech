#!/bin/sh
set -e

HOST=oscar-db-0.oscar-db.oscar-emr.svc.cluster.local

# Function to run SQL and allow ERROR 1050
run_sql() {
    FILE="$1"
    echo "▶️ Running $FILE ..."
    ERR=$(mysql -h "$HOST" -u "$USER" -p"$PASS" "$DB" < "$FILE" 2>&1) || true
    if echo "$ERR" | grep -q "ERROR"; then
        if echo "$ERR" | grep -q "ERROR 1050"; then
            echo "⚠️ Table already exists (safe to ignore)"
        else
            echo "❌ Unhandled SQL error in $FILE:"
            echo "$ERR"
            exit 1
        fi
    else
        echo "✅ $FILE completed successfully"
    fi
}

run_sql /migrations/oscarinit.sql
run_sql /migrations/oscardata.sql
run_sql /migrations/initcaisi.sql
run_sql /migrations/initcaisi_data.sql
run_sql /migrations/patch19.sql

echo "🎉 All migrations completed."
