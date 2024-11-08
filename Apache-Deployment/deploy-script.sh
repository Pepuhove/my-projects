#!/bin/bash

# Check if URL and filename arguments are provided
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: deploy_script.sh <URL> <filename>"
  exit 1
fi

URL=$1
FILENAME=$2

echo "Installing and Starting HTTPD Service..."
systemctl start httpd && systemctl enable httpd

# Create a temporary directory for downloading files
mkdir -p /tmp/webfiles && cd /tmp/webfiles

# Download and deploy web files
wget $URL -O "$FILENAME.zip"
unzip "$FILENAME.zip"
cp -r "$FILENAME"/* /var/www/html/

# Clean up
rm -rf /tmp/webfiles
echo "Deployment completed!"
