#!/usr/bin/env python3

import json
import sys

def create_template_config(input_file, output_file):
    """
    Convert a CloudFormation parameters file to a template configuration file
    for use with CodePipeline's TemplateConfiguration parameter.
    """
    # Read the CloudFormation parameters file
    with open(input_file, 'r') as f:
        params = json.load(f)
    
    # Convert to the format expected by TemplateConfiguration
    param_dict = {}
    for param in params:
        param_dict[param['ParameterKey']] = param['ParameterValue']
    
    # Create the template configuration structure
    template_config = {
        "Parameters": param_dict
    }
    
    # Write the template configuration to a new file
    with open(output_file, 'w') as f:
        json.dump(template_config, f, indent=2)
    
    print(f"Template configuration saved to {output_file}")
    print("Use this file with CodePipeline's TemplateConfiguration parameter")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_params.json> <output_template_config.json>")
        sys.exit(1)
    
    create_template_config(sys.argv[1], sys.argv[2])
