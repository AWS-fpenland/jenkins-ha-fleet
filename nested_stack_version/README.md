# Jenkins High Availability with FIS Testing - Nested Stack

## Overview

This project provides a nested CloudFormation stack that deploys both a highly available Jenkins environment and AWS Fault Injection Simulator (FIS) resources for testing resilience. The architecture uses EC2 instances for Jenkins controllers behind an Application Load Balancer, with EC2 Fleet for worker nodes, shared EFS storage for persistence, and FIS for simulating Insufficient Capacity Errors (ICE).

## Architecture

The nested stack consists of:

1. **Main Stack**: Orchestrates the deployment of both Jenkins and FIS stacks
2. **Jenkins Stack**: Deploys the Jenkins HA infrastructure
3. **FIS Stack**: Deploys the FIS experiment resources for testing

### Jenkins Stack Resources

- **Networking**: A complete VPC setup with public and private subnets across 3 availability zones, NAT gateways, and proper routing
- **Security**: Dedicated security groups for each component with least-privilege access
- **Storage**: Amazon EFS for persistent Jenkins home directory
- **Compute**: Auto Scaling Group for Jenkins controllers and EC2 Fleet for worker nodes
- **IAM**: Appropriate IAM roles and instance profiles
- **Load Balancing**: Application Load Balancer for distributing traffic to controllers

### FIS Stack Resources

- **S3 Bucket**: For storing FIS experiment reports
- **CloudWatch**: Log groups, metric filters, and dashboards for monitoring ICE events
- **IAM**: Roles and policies for FIS experiments
- **FIS Experiment Template**: Configured to simulate ICE in a specific availability zone

## Deployment

### Prerequisites

- An AWS account with permissions to create the resources in the template
- AWS CLI or AWS Console access

### Deployment Steps

1. Navigate to AWS CloudFormation in the AWS Console
2. Choose "Create stack" > "With new resources"
3. Upload the `main-stack.yaml` file
4. Provide parameters as needed
5. Review and create the stack

### Parameters

The main stack accepts parameters that are passed to both the Jenkins and FIS stacks:

| Parameter | Description | Default |
|-----------|-------------|---------|
| EnvironmentName | Name for the environment (used for resource tagging) | jenkins-poc |
| JenkinsVersion | Version of Jenkins to install | 2.426.1 |
| LatestAmiId | Amazon Linux 2 AMI ID parameter | /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 |
| LogRetentionInDays | Number of days to retain logs in CloudWatch | 30 |
| ExperimentDuration | Duration of the FIS experiment | PT30M (30 minutes) |
| AvailabilityZone | AZ identifier to simulate ICE | usw2-az2 |

## Post-Deployment Steps

### Accessing Jenkins

1. After deployment completes, find the Jenkins URL in the CloudFormation outputs
2. Access Jenkins through the ALB DNS name (http://[ALB-DNS-NAME])
3. Retrieve the initial admin password from SSM Parameter Store at `/${EnvironmentName}/jenkins/initial-admin-password`

### Running FIS Experiments

1. Navigate to the AWS FIS console
2. Find the experiment template created by the stack
3. Start the experiment to simulate ICE in the specified availability zone
4. Monitor the results in the CloudWatch dashboard (URL provided in stack outputs)

## Maintenance and Troubleshooting

### Updating the Stack

To update any component:

1. Make changes to the relevant template file
2. Update the stack in CloudFormation

### Troubleshooting

- Check CloudFormation events for deployment issues
- Review CloudWatch logs for Jenkins and FIS components
- Examine the FIS experiment history for test results

## Security Considerations

- The template restricts HTTP/HTTPS access to a specific IP (`69.126.73.111/32`) - update this for your environment
- SSH access is currently open (`0.0.0.0/0`) and should be restricted to specific IPs or bastion hosts
- Consider implementing HTTPS with ACM for the ALB

## Resource Cleanup

To remove all resources:

1. Delete the main CloudFormation stack
2. This will automatically delete all nested stacks and their resources
