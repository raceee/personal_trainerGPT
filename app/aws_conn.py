import boto3
import json

def get_secret(secret_name='trainergpt_secret'):

    client = boto3.client(
        service_name='secretsmanager',
        region_name='us-east-1'
    )

    response = client.get_secret_value(
        SecretId=secret_name
    )

    chatgpt_secret = json.loads(response['SecretString'])

    return chatgpt_secret