# Example using async credentials and application access.
from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient

credential = ClientSecretCredential(
    tenant_id='9a6aeee0-b1b6-40c3-a26f-03927944a519',
    client_id='48caa542-6d01-49a0-83a7-8f9c2e414a3e',
    client_secret='8LJ8Q~O284xXYFy6BheqCK5Yvji2tkMLgs6WlaMI',
)
scopes = ['https://graph.microsoft.com/.default']
client = GraphServiceClient(credential=credential, scopes=scopes)