# Use a smaller Alpine base image
FROM alpine:latest

# Install only the necessary packages
RUN apk update && \
    apk add --no-cache wget apache2 unzip bash vim && \
    rm -rf /var/cache/apk/*  # Clean up package manager cache

# Copy the deploy script into the container
COPY deploy_script.sh /usr/local/bin/deploy_script.sh

# Make the script executable
RUN chmod +x /usr/local/bin/deploy_script.sh

# Expose the HTTP port
EXPOSE 80

# Use an entrypoint to pass arguments to the deploy script
ENTRYPOINT ["/bin/bash", "/usr/local/bin/deploy_script.sh"]
