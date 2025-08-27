#!/usr/bin/env python3
"""
Minimal chat script demonstrating AWS Bedrock Opus 4 model using the converse api.
"""

import boto3

MODEL_NAME = 'model'
MODEL_ID = 'us.anthropic.claude-opus-4-20250514-v1:0'
AWS_REGION = 'us-east-2'

INFERENCE_CONFIG = {
    "maxTokens": 4096,
    "temperature": 0.7,
    "topP": 0.9
}

def chat_with_nova():
    client = boto3.client('bedrock-runtime', region_name=AWS_REGION)
    conversation = []
    
    print(f"Chat with {MODEL_NAME} (type 'quit' to exit)")
    print("-" * 50)
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
        
        conversation.append({
            "role": "user",
            "content": [{"text": user_input}]
        })
        
        try:
            response = client.converse(
                modelId=MODEL_ID,
                messages=conversation,
                inferenceConfig=INFERENCE_CONFIG
            )
            
            assistant_message = response['output']['message']
            assistant_text = assistant_message['content'][0]['text']
            conversation.append(assistant_message)
            print(f"\n{MODEL_NAME}: {assistant_text}")
            
        except Exception as e:
            print(f"\nError: {e}")
            conversation.pop()

if __name__ == "__main__":
    chat_with_nova()