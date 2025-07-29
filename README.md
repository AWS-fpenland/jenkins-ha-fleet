# Jenkins High Availability on AWS

## Overview

This CloudFormation template deploys a highly available Jenkins environment on AWS. The architecture uses EC2 instances for Jenkins controllers behind an Application Load Balancer, with EC2 Fleet for worker nodes and shared EFS storage for persistence.

## Architecture

The template creates the following resources:

- **Networking**: A complete VPC setup with public and private subnets across 3 availability zones, NAT gateways, and proper routing
- **Security**: Dedicated security groups for each component with least-privilege access
- **Storage**: Amazon EFS for persistent Jenkins home directory
- **Compute**: Auto Scaling Group for Jenkins controllers and EC2 Fleet for worker nodes
- **IAM**: Appropriate IAM roles and instance profiles
- **Load Balancing**: Application Load Balancer for distributing traffic to controllers

## Prerequisites

- An AWS account with permissions to create the resources in the template
- AWS CLI or AWS Console access

## Deployment

### Quick Start

1. Navigate to AWS CloudFormation in the AWS Console
2. Choose "Create stack" > "With new resources"
3. Upload the `jenkins-stack.yaml` file
4. Provide parameters as needed
5. Review and create the stack

### Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| EnvironmentName | Name for the environment (used for resource tagging) | jenkins-poc |
| JenkinsVersion | Version of Jenkins to install | 2.426.1 |
| LatestAmiId | Amazon Linux 2 AMI ID parameter | /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 |

## Features

### Auto-Generated SSH Key Pair

The template automatically creates an SSH key pair and stores the fingerprint in AWS Secrets Manager, eliminating the need to manually create and manage keys.

### High Availability

- Controllers deployed across multiple availability zones
- EFS shared storage for Jenkins home
- Load balancer for traffic distribution

### Scalability

- Auto Scaling Group for Jenkins controllers
- EC2 Fleet for dynamic worker provisioning based on demand
- Instance type diversification for both availability and cost optimization

### Security

- Private subnets for Jenkins controllers and workers
- Restricted security groups with least-privilege access
- Systems Manager for secure instance access
- Secrets Manager for credential storage
- IMDSv2 enforcement via metadata options

## Post-Deployment Steps

### Accessing Jenkins

1. After deployment completes, find the Jenkins URL in the CloudFormation outputs
2. Access Jenkins through the ALB DNS name (http://[ALB-DNS-NAME])
3. Retrieve the initial admin password:
   - From SSM Parameter Store at `/${EnvironmentName}/jenkins/initial-admin-password`
   - From the EC2 instance at `/var/lib/jenkins/secrets/initialAdminPassword`

### Jenkins Configuration

1. Complete the initial Jenkins setup through the web interface
2. Install recommended plugins
3. Configure the EC2 Fleet Plugin to connect to your worker fleet:
   - Install "Amazon EC2 Fleet Plugin" through the Jenkins plugin manager
   - Configure the plugin to use the EC2 Fleet ID from the CloudFormation outputs

## Worker Nodes Configuration

The worker nodes are provisioned with:

- Java 11 (Amazon Corretto)
- Git
- Docker
- Python 3
- Maven

You can customize the worker configuration by modifying the UserData section in the `WorkerLaunchTemplate` resource.

## Maintenance

### Updating Jenkins

To update Jenkins version:

1. Update the `JenkinsVersion` parameter
2. Update the stack in CloudFormation

### Backups

The Jenkins configuration is stored on EFS, which provides durability. For additional protection:

1. Create regular EFS snapshots
2. Implement a backup solution for critical Jenkins data

### Monitoring

Consider setting up:

1. CloudWatch alarms for instance health
2. CloudWatch dashboards for resource utilization
3. AWS Systems Manager for patching and compliance

## Security Considerations

- The template restricts HTTP/HTTPS access to a specific IP (`69.126.73.111/32`) - update this for your environment
- SSH access is currently open (`0.0.0.0/0`) and should be restricted to specific IPs or bastion hosts
- Consider implementing HTTPS with ACM for the ALB
- Review IAM permissions for least privilege

## Cost Management

- Worker nodes use EC2 Fleet with Spot instances for cost optimization
- Instance types are diversified to improve Spot availability
- Consider scheduling the EC2 Fleet to scale down during off-hours

## Troubleshooting

### Common Issues

1. **Jenkins fails to start**: Check instance CloudWatch logs and systemd logs (`journalctl -u jenkins`)
2. **EFS mount issues**: Verify security groups and mount commands in user data
3. **Worker connections failing**: Check security group rules and JNLP port configuration

### Logs

Important log locations:
- Jenkins: `/var/log/jenkins/jenkins.log`
- System: `/var/log/messages`
- Cloud-init: `/var/log/cloud-init.log` and `/var/log/cloud-init-output.log`

## Resource Cleanup

To remove all resources:

1. Delete the CloudFormation stack
2. Check for any resources that may need manual cleanup (e.g., snapshots)

## Customization

### Template Modifications

Key areas for customization:

- `JenkinsLaunchTemplate`: Modify user data to install additional tools
- `WorkerLaunchTemplate`: Customize worker node configuration
- `EC2FleetConfiguration`: Adjust instance types and allocation strategy
- `ALBSecurityGroup`: Update allowed IP ranges

## License

This template is provided under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
