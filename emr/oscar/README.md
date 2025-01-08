
1. Build OSCAR image: `docker-compose build`.
2. Start everything: `docker-compose up`.
3. Check logs: `docker-compose logs -f`.

Go to: http://localhost:8201/oscar

To SSH into the container: `docker exec -it oscar bash`.

`docker-compose logs db`

## First Sign In

1. Username: `oscardoc`.
2. Password: `mac2002`.
3. PIN: `1117`.

## Migrations

#Warning: World-writable config file '/etc/mysql/conf.d/my.cnf' is ignored

```bash
docker-compose up -d db

# Copy the SQL files to the DB container
docker cp migrations/oscarinit.sql oscar-db:/oscarinit.sql
docker cp migrations/oscardata.sql oscar-db:/oscardata.sql
docker cp migrations/patch19.sql oscar-db:/patch19.sql

docker-compose exec db bash

# Then inside the DB container:
# OPTIONAL: mysql -u oscar -p'oscarpw' -e "DROP DATABASE oscar; CREATE DATABASE oscar;"
mysql -u oscar -p'oscarpw' oscar < /oscarinit.sql
mysql -u oscar -p'oscarpw' oscar < /oscardata.sql
mysql -u oscar -p'oscarpw' oscar < /initcaisi.sql
mysql -u oscar -p'oscarpw' oscar < /initcaisi_data.sql
mysql -u oscar -p'oscarpw' oscar < /patch19.sql

# Or just the following for any arbitrary SQL commands:
mysql -u oscar -p'oscarpw' oscar
```


# conf/context.xml
