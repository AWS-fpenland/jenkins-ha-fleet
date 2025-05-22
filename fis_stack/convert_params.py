#!/usr/bin/env python3

import json
import sys

def convert_params(input_file, output_file):
    # Read the CloudFormation parameters file
    with open(input_file, 'r') as f:
        params = json.load(f)
    
    # Convert to the format expected by ParameterOverrides
    param_overrides = {}
    for param in params:
        param_overrides[param['ParameterKey']] = param['ParameterValue']
    
    # Write the converted parameters to a new file
    with open(output_file, 'w') as f:
        json.dump(param_overrides, f)
    
    print(f"Converted parameters saved to {output_file}")
    print(f"Use this content directly in the ParameterOverrides field in CodePipeline")
    
    # Also print the JSON string that can be used directly
    print("\nJSON string for direct use in ParameterOverrides:")
    print(json.dumps(param_overrides))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_params.json> <output_params.json>")
        sys.exit(1)
    
    convert_params(sys.argv[1], sys.argv[2])
