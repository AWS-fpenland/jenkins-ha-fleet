# FIS Stack Deployment Guide

## Using Parameters with CodePipeline

When deploying this CloudFormation stack via CodePipeline, you need to use the correct parameter format.

### Option 1: Update the Pipeline in AWS Console

1. Go to the AWS CodePipeline console
2. Select your pipeline (`fis-stack-Pipeline-f1c4dab8`)
3. Click "Edit"
4. Edit the CloudFormation action in the Deploy stage
5. Replace the `ParameterOverrides` value with the following JSON string:

```json
{"EnvironmentName": "fis-stack", "AutoScalingGroupName": "ice-poc-v2-jenkins-workers", "ASGResourceId": "a435d023-5b08-4534-9c51-97ee2e448d9b", "LogRetentionInDays": "30", "ExperimentDuration": "PT30M", "AvailabilityZone": "use1-az6", "ExistingCloudTrailLogGroup": "aws-controltower/CloudTrailLogs", "InstanceType1": "r6a.large", "InstanceType2": "m6a.large", "InstanceType3": "r6a.xlarge", "InstanceType4": "c6a.large", "InstanceType5": "m6a.xlarge", "InstanceType6": "c6a.xlarge"}
```

### Option 2: Create a New Pipeline

If you want to create a new pipeline, you can use the `pipeline-deploy.py` script with the following changes:

1. When prompted for parameters, choose option 2 (Local parameters file)
2. Provide the path to your parameters.json file
3. The script will automatically convert the parameters to the correct format

### Option 3: Use Template Configuration File

Alternatively, you can create a template configuration file that includes both parameters and stack configuration:

1. Create a file named `template-configuration.json` with the following content:

```json
{
  "Parameters": {
    "EnvironmentName": "fis-stack",
    "AutoScalingGroupName": "ice-poc-v2-jenkins-workers",
    "ASGResourceId": "a435d023-5b08-4534-9c51-97ee2e448d9b",
    "LogRetentionInDays": "30",
    "ExperimentDuration": "PT30M",
    "AvailabilityZone": "use1-az6",
    "ExistingCloudTrailLogGroup": "aws-controltower/CloudTrailLogs",
    "InstanceType1": "r6a.large",
    "InstanceType2": "m6a.large",
    "InstanceType3": "r6a.xlarge",
    "InstanceType4": "c6a.large",
    "InstanceType5": "m6a.xlarge",
    "InstanceType6": "c6a.xlarge"
  }
}
```

2. Commit this file to your repository
3. Update the pipeline to use `TemplateConfiguration` instead of `ParameterOverrides`
