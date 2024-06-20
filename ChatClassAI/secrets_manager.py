import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def get_secret():
    # Para testes, retorne uma chave de API fictícia
    return "test_openai_api_key"
    # Caso queira testar a lógica real, descomente as linhas abaixo e forneça os valores corretos
    """
    secret_name = "YOUR_SECRET_NAME"
    region_name = "YOUR_AWS_REGION"

    # Cria um cliente
    client = boto3.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret = get_secret_value_response['SecretString']
        return secret
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Credentials error: {e}")
        return None
    """
