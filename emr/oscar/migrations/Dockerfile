FROM mariadb:10.6

# Copy SQL files into image
COPY oscarinit.sql oscardata.sql initcaisi.sql initcaisi_data.sql patch19.sql /migrations/

# Use bash shell by default
CMD ["bash"]
