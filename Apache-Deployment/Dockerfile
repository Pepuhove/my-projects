# Use an official Ubuntu base image
FROM ubuntu:latest

# Update the OS and install necessary packages
RUN apt update -y && \
    apt install -y wget apache2 unzip vim && \
    apt clean all

# Copy the deploy_script.sh into the container
COPY deploy_script.sh /usr/local/bin/deploy_script.sh

# Make the script executable
RUN chmod +x /usr/local/bin/deploy_script.sh

# Expose the default HTTP port (Apache)
EXPOSE 80

# Run Apache and the deploy script with arguments
CMD ["/bin/bash", "/usr/local/bin/deploy_script.sh", "https://www.tooplate.com/zip-templates/2131_wedding_lite.zip", "2131_wedding_lite"]
