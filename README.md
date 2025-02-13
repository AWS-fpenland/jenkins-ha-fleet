# Repository Structure

```
jenkins-ha-fleet/
├── README.md
├── templates/
│   ├── master-stack.yaml       # Main stack template
│   ├── network-stack.yaml      # Network infrastructure
│   ├── security-stack.yaml     # Security and IAM roles
│   ├── jenkins-controller.yaml # Jenkins controller configuration
│   └── jenkins-workers.yaml    # EC2 Fleet worker configuration
└── deployment/
    └── stack-deployment.yaml   # Stack deployment configuration file
```

# Stack Deployment File (deployment/stack-deployment.yaml)

deploymentParameters:
  stackName: jenkins-ha-fleet
  template: templates/master-stack.yaml
  capabilities:
    - CAPABILITY_NAMED_IAM
  parameters:
    - key: EnvironmentName
      value: jenkins-poc
    - key: KeyName
      value: your-key-pair-name  # Replace with your EC2 key pair name
  tags:
    - key: Environment
      value: POC
    - key: Project
      value: JenkinsHA
    - key: ManagedBy
      value: CloudFormation

# README.md

# Jenkins HA with EC2 Fleet

This repository contains CloudFormation templates for deploying a highly available Jenkins setup with EC2 Fleet for worker nodes.

## Deployment Instructions

1. Create a GitHub repository and push this code structure to it

2. In the AWS Console:
   - Go to CloudFormation > Create Stack > With new resources
   - Choose "Sync from Git" as template source
   - Link your GitHub repository:
     - Choose GitHub as repository provider
     - Create/select a CodeStar connection
     - Select the repository and main branch
     - Set deployment file path to: deployment/stack-deployment.yaml
     - Set template file path to: templates/master-stack.yaml

3. Set stack parameters:
   - Stack name: jenkins-ha-fleet
   - Environment name: jenkins-poc
   - Key pair name: your-ec2-key-pair

4. Review and create the stack

5. Merge the automatically created pull request in your GitHub repository

## Making Changes

1. Make changes to templates in your repository
2. Commit and push to the monitored branch
3. CloudFormation will automatically create a pull request with the changes
4. Review and merge the pull request to apply the changes

## Repository Files

- `templates/`: Contains all CloudFormation templates
- `deployment/`: Contains the stack deployment configuration
- `README.md`: Documentation and deployment instructions

## Template Structure

- `master-stack.yaml`: Main stack that orchestrates all other stacks
- `network-stack.yaml`: VPC, subnets, and networking components
- `security-stack.yaml`: IAM roles and security groups
- `jenkins-controller.yaml`: Jenkins controller configuration
- `jenkins-workers.yaml`: EC2 Fleet worker configuration