import boto3
import base64


def get_secret(secret_name):

    region_name = "us-east-1"

    # Create Secrets Manager Client

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )

    if 'SecretString' in secret_value_response:
        secret = secret_value_response['SecretString']

        return eval(secret)

    else:
        decoded_binary_secret = base64.b64encode(secret_value_response['SecretBinary'])
        return decoded_binary_secret

