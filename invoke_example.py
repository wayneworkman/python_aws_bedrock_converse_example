#!/usr/bin/env python3
"""
Minimal chat script demonstrating AWS Bedrock Nova Lite model using the invoke api.
"""

import boto3
import json

MODEL_NAME = 'Amazon Nova Lite'
MODEL_ID = 'us.amazon.nova-lite-v1:0'
AWS_REGION = 'us-east-2' 

INFERENCE_CONFIG = {
    "max_tokens": 4096,
    "temperature": 0.7
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
            request_body = {
                "messages": conversation,
                "inferenceConfig": {
                    "maxTokens": INFERENCE_CONFIG["max_tokens"],
                    "temperature": INFERENCE_CONFIG["temperature"]
                }
            }
            
            response = client.invoke_model(
                modelId=MODEL_ID,
                body=json.dumps(request_body),
                contentType='application/json',
                accept='application/json'
            )
            
            response_body = json.loads(response['body'].read())
            
            if 'output' in response_body and 'message' in response_body['output']:
                assistant_text = response_body['output']['message']['content'][0]['text']
            else:
                assistant_text = response_body.get('completion', 'No response text found')
            
            conversation.append({
                "role": "assistant",
                "content": [{"text": assistant_text}]
            })
            
            print(f"\n{MODEL_NAME}: {assistant_text}")
            
        except Exception as e:
            print(f"\nError: {e}")
            conversation.pop()

if __name__ == "__main__":
    chat_with_nova()