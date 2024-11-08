# Use an official CentOS or Amazon Linux base image, depending on your environment needs
FROM ubuntu:latest

# Update the OS and install necessary packages
RUN apt update -y && \
    apt install -y wget httpd unzip vim && \
    apt clean all

# Copy the script into the container
COPY deploy_script.sh /usr/local/bin/deploy_script.sh

# Make the script executable
RUN chmod +x /usr/local/bin/deploy_script.sh

# Set up Apache to run in the background
RUN echo "daemon off;" >> /etc/httpd/conf/httpd.conf

# Expose the default HTTP port
EXPOSE 80

# Start the Apache server by default
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
