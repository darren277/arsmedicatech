
1. Build OSCAR image: `docker-compose build`.
2. Start everything: `docker-compose up`.
3. Check logs: `docker-compose logs -f`.

Go to: http://localhost:8085/oscar

To SSH into the container: `docker exec -it oscar bash`.

`docker-compose logs db`

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
mysql -u oscar -p'oscarpw' oscar < /patch19.sql
```


# cat conf/context.xml
<?xml version="1.0" encoding="UTF-8"?>
<!--
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<!-- The contents of this file will be loaded for each web application -->
<Context>

    <!-- Default set of monitored resources. If one of these changes, the    -->
    <!-- web application will be reloaded.                                   -->
    <WatchedResource>WEB-INF/web.xml</WatchedResource>
    <WatchedResource>WEB-INF/tomcat-web.xml</WatchedResource>
    <WatchedResource>${catalina.base}/conf/web.xml</WatchedResource>

    <!-- Uncomment this to disable session persistence across Tomcat restarts -->
    <!--
    <Manager pathname="" />
    -->


    <Resources cacheMaxSize="100000" />
</Context>
