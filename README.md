AWS VPC Setup with EC2 Web Server using Terraform
This project automates the deployment of a Virtual Private Cloud (VPC) on AWS, provisioning necessary networking components and launching an EC2 instance as a web server. The configuration uses Terraform to establish a secure and scalable environment for hosting a sample web application.

Project Overview
The infrastructure setup includes:

VPC with a designated CIDR block.
Internet Gateway to enable internet access for resources within the VPC.
Route Table with routes for both IPv4 and IPv6 traffic.
Public Subnet associated with the route table.
Security Group allowing web (HTTP/HTTPS) and SSH traffic.
Elastic IP assigned to the EC2 instance.
Network Interface associated with the Elastic IP and Security Group.
EC2 Instance (Ubuntu) hosting a web server with a sample website.
Key Components
VPC and Networking:

A VPC with public subnet and internet gateway.
Route table for internet access and secure communication.
Security Group:

Allows inbound HTTP (80), HTTPS (443), and SSH (22) traffic.
Egress traffic is unrestricted for outbound connectivity.
EC2 Instance:

Ubuntu server with Apache web server installed.
User data script to download and host a sample HTML template.
Prerequisites
AWS Account with permissions for creating VPCs, EC2 instances, and related resources.
Terraform installed on your local machine.
Usage
Clone the repository:
bash
Copy code
git clone https://github.com/Pepuhove/aws-vpc-setup.git
Initialize and apply the Terraform configuration:
bash
Copy code
cd aws-vpc-setup
terraform init
terraform apply
Confirm the output and navigate to the provided IP address to view the hosted website.
Directory Structure
graphql
Copy code
aws-vpc-setup/
├── main.tf            # Main configuration file
├── variables.tf       # Variables for AWS region and VPC settings
├── outputs.tf         # Outputs for generated resources (e.g., EC2 IP)
└── README.md          # Project description
