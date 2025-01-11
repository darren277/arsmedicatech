FROM tomcat:9.0-jdk11

# Copy the OSCAR WAR into Tomcat's webapps folder.
# Adjust the name of the WAR file to match your build.
#https://bitbucket.org/oscaremr/oscar/downloads/oscar-19.4690.war
RUN wget -O /usr/local/tomcat/webapps/oscar.war https://bitbucket.org/oscaremr/oscar/downloads/oscar-19.4690.war
##COPY oscar-19.war /usr/local/tomcat/webapps/oscar.war

RUN apt-get update && apt-get install -y vim nano wget mariadb-client && rm -rf /var/lib/apt/lists/*


# 1) Manually unzip the WAR so that /WEB-INF/classes/ actually exists
RUN apt-get update && apt-get install -y unzip && rm -rf /var/lib/apt/lists/*
RUN mkdir /usr/local/tomcat/webapps/oscar && unzip /usr/local/tomcat/webapps/oscar.war -d /usr/local/tomcat/webapps/oscar && rm /usr/local/tomcat/webapps/oscar.war

# 2) Now that the WAR is expanded, we can patch the file
#RUN sed -i "s|^db_username\s*=.*|db_username = oscar|" /usr/local/tomcat/webapps/oscar/WEB-INF/classes/oscar_mcmaster.properties && sed -i "s|^db_password\s*=.*|db_password = oscarpw|" /usr/local/tomcat/webapps/oscar/WEB-INF/classes/oscar_mcmaster.properties

#ARG DB_HOST
#ARG DB_PORT
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD
#ARG TZ

# Path inside the WAR deployment; you might need to expand the WAR first or rely on Tomcat’s auto-expansion
ENV OSCAR_PROPS="/usr/local/tomcat/webapps/oscar/WEB-INF/classes/oscar_mcmaster.properties"

# Use sed (or similar) to replace lines
RUN sed -i "s|^db_name\s*=.*|db_name = $DB_NAME|" "$OSCAR_PROPS"
RUN sed -i "s|^db_username\s*=.*|db_username = $DB_USER|" "$OSCAR_PROPS"
RUN sed -i "s|^db_password\s*=.*|db_password = $DB_PASSWORD|" "$OSCAR_PROPS"
RUN sed -i "s|^db_uri\s*=.*|db_uri = jdbc:mysql://db:3306/|" "$OSCAR_PROPS"

# billregion=ON => billregion=BC
RUN sed -i "s|^billregion=ON|billregion=BC|" "$OSCAR_PROPS"


#RUN echo "db_host = $DB_HOST" >> "$OSCAR_PROPS"
#RUN echo "db_port = $DB_PORT" >> "$OSCAR_PROPS"
RUN echo "\n\ndb_name = $DB_NAME" >> "$OSCAR_PROPS"
RUN echo "db_username = $DB_USER" >> "$OSCAR_PROPS"
RUN echo "db_password = $DB_PASSWORD" >> "$OSCAR_PROPS"
#RUN echo "db_uri = jdbc:mysql://$DB_HOST:$DB_PORT/" >> "$OSCAR_PROPS"
#jdbc:mysql://db:3306/
RUN echo "db_uri = jdbc:mysql://db:3306/" >> "$OSCAR_PROPS"

# billregion=ON => billregion=BC
RUN echo "billregion=BC" >> "$OSCAR_PROPS"

#COPY oscar.properties /usr/local/tomcat/conf/oscar.properties

COPY ./conf/context.xml /usr/local/tomcat/conf/context.xml

# Copy entrypoint script into container
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose Tomcat HTTP on 8080 (and optionally 8443 for HTTPS if you want to self-sign)
EXPOSE 8080
EXPOSE 8201
EXPOSE 8443

# Use the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
