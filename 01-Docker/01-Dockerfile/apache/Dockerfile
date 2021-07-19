# Base Image 
FROM ubuntu:16.04

# Maintainer
MAINTAINER Amit <amitvashist7@outlook.com>

# Update APT Repo
RUN apt-get update

#Install Apache2 Packages
RUN apt-get install apache2 -y 

# Expose 
EXPOSE 80 
EXPOSE 3306 

# Custom Web Page Deployment
COPY index.html /var/www/html/

# Bring up Apache Service
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
