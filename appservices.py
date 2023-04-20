from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient

subscription_id = 'xxxxxx'
client_id = 'xxxxxx'
client_secret = 'xxxxxx'
tenantid = 'xxxxxx'

credentials = ClientSecretCredential(
    tenant_id=tenantid, 
    client_id=client_id, 
    client_secret=client_secret
)

web_client = WebSiteManagementClient(credentials, subscription_id)

#Imprimir o nome de cada AppService
webapps = web_client.web_apps.list()
for webapp in webapps:
    print(webapp.name)

#Contar o número total de AppService
webapps = web_client.web_apps.list()
count = sum(1 for _ in webapps)
print("Numero total de App Services:", count)