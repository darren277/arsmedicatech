#!/usr/bin/env bash
set -e

# Optional: If you keep an oscar.properties template inside the container,
# you can do environment variable substitution here.
# For example, if /usr/local/tomcat/conf/oscar.properties.template
# contains placeholders like DB_HOST={{DB_HOST}}, you can do:
#
# sed -i "s|{{DB_HOST}}|${DB_HOST}|g" /usr/local/tomcat/conf/oscar.properties.template
# sed -i "s|{{DB_NAME}}|${DB_NAME}|g" /usr/local/tomcat/conf/oscar.properties.template
# sed -i "s|{{DB_USER}}|${DB_USER}|g" /usr/local/tomcat/conf/oscar.properties.template
# sed -i "s|{{DB_PASSWORD}}|${DB_PASSWORD}|g" /usr/local/tomcat/conf/oscar.properties.template
#
# mv /usr/local/tomcat/conf/oscar.properties.template /usr/local/tomcat/conf/oscar.properties

# Optionally set the container's timezone
ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone

# Start Tomcat
exec catalina.sh run
