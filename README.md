# AWS Bedrock Converse API Example

A minimal Python script demonstrating how to use AWS Bedrock's Converse API with conversation context tracking.

## Purpose

This script serves as a quick reference implementation showing:
- How to use the AWS Bedrock Converse API
- How to maintain conversation context across multiple interactions
- Proper message format for the Converse API
- Basic error handling for API calls

## Features

- Interactive chat interface with AWS Bedrock Nova model
- Maintains full conversation history for contextual responses
- Simple configuration through constants
- Clean error handling

## Default Configuration

The script is configured by default to use:
- **Region**: `us-east-2`
- **Model**: Nova Lite (`us.amazon.nova-lite-v1:0`)

### About Nova Lite

As of August 14, 2025, Nova Lite costs:
- **Input**: $0.00006 per 1K tokens
- **Output**: $0.00024 per 1K tokens

To put this in perspective: generating a standard 80,000-word novel (~100K tokens) would cost approximately $0.024 (2.4 cents) in output tokens. Nova Lite is one of the cheapest models available on AWS Bedrock, making it ideal for learning purposes and very light workloads.

## Requirements

- Python 3.x
- boto3 library
- AWS credentials configured with access to Bedrock
- **Important**: You must enable the Nova Lite model in AWS Bedrock before using this script

### AWS Permissions

The minimum IAM permissions required to run this script:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": "arn:aws:bedrock:us-east-2:*:foundation-model/us.amazon.nova-lite-v1:0"
        }
    ]
}
```

## Usage

```bash
python converse_example.py
```

Type `quit`, `exit`, or `bye` to end the conversation.

## Configuration

The script uses the following configurable constants:
- `MODEL_NAME`: Display name for the model (default: 'Nova')
- `MODEL_ID`: AWS Bedrock model identifier (default: Nova Lite)
- `AWS_REGION`: AWS region for Bedrock service (default: us-east-2)
- `INFERENCE_CONFIG`: Model inference parameters
  - `maxTokens`: 4096 (maximum response length)
  - `temperature`: 0.7 (creativity/randomness level)
  - `topP`: 0.9 (nucleus sampling parameter)

## License

See the LICENSE file for licensing information.