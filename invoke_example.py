#!/usr/bin/env python3
"""
Minimal chat script demonstrating AWS Bedrock Opus 4 model using the invoke api.
"""

import boto3
import json

MODEL_NAME = 'model'
MODEL_ID = 'us.anthropic.claude-opus-4-20250514-v1:0'
AWS_REGION = 'us-east-2' 

INFERENCE_CONFIG = {
    "max_tokens": 4096,
    "temperature": 0.7,
    "top_p": 0.9,
    "anthropic_version": "bedrock-2023-05-31"
}

def chat_with_claude():
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
            "content": user_input
        })
        
        try:
            request_body = {
                "anthropic_version": INFERENCE_CONFIG["anthropic_version"],
                "max_tokens": INFERENCE_CONFIG["max_tokens"],
                "temperature": INFERENCE_CONFIG["temperature"],
                "top_p": INFERENCE_CONFIG["top_p"],
                "messages": conversation,
                "system": ""
            }
            
            response = client.invoke_model(
                modelId=MODEL_ID,
                body=json.dumps(request_body),
                contentType='application/json',
                accept='application/json'
            )
            
            response_body = json.loads(response['body'].read())
            
            if 'content' in response_body:
                assistant_text = response_body['content'][0]['text']
            else:
                assistant_text = response_body.get('completion', 'No response text found')
            
            conversation.append({
                "role": "assistant",
                "content": assistant_text
            })
            
            print(f"\n{MODEL_NAME}: {assistant_text}")
            
        except Exception as e:
            print(f"\nError: {e}")
            conversation.pop()

if __name__ == "__main__":
    chat_with_claude()