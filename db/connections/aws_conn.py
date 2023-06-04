import boto3
import json



def get_secret(secret_name='trainergpt_db'):

    client = boto3.client('secretsmanager')
    response = client.get_secret_value(
        SecretId=secret_name
    )
    database_secrets = json.loads(response['SecretString'])

    return database_secrets
