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


#### Retrive jenkins secret

```
aws secretsmanager get-secret-value \
    --secret-id jenkins-poc-jenkins-admin-credentials \
    --query SecretString --output text | jq -r '.password' \
    --profile netcore
```

0cba67150ee74a318e846ace16e7fc56

http://jenkins-poc-jenkins-alb-2014278711.us-east-1.elb.amazonaws.com/

3Y1xW]4I_md:D$ep

aws autoscaling set-desired-capacity \
    --auto-scaling-group-name jenkins-poc-jenkins-controllers \
    --desired-capacity 2 \
    --region us-east-1 \
    --profile netcore


java -jar jenkins-plugin-manager-*.jar --war /your/path/to/jenkins.war --plugin-download-directory /your/path/to/plugins/ --plugin-file /your/path/to/plugins.txt --plugins delivery-pipeline-plugin:1.3.2 deployit-plugin


aws ssm get-parameter \
  --name "/jenkins-poc/jenkins/initial-admin-password" \
  --with-decryption \
  --query "Parameter.Value" \
  --output text \
  --profile netcore

  61ab90534547451aadd7d9370a90a89b

  aws ssm get-parameter --name "/jenkins-poc/jenkins/initial-admin-password" --with-decryption --query "Parameter.Value" --output text --profile netcore


i-015a4a357388ff082 - Working Jenkins Instance