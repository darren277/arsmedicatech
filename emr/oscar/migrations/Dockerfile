FROM alpine:3.19

RUN apk add --no-cache bash mysql-client libc6-compat

# Copy SQL files into image
COPY oscarinit.sql oscardata.sql initcaisi.sql initcaisi_data.sql patch19.sql /migrations/

# Use bash shell by default
CMD ["bash"]
