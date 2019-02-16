# Upload File's to Google Storage - Python


## English

## Operating Flow:

For this example, the Tornado http framework was used, so we can traffic the client base64 data to this service.

However this service can be adapted to any REST API or other HTTP services developed in Python.



* Create your storage credentials key file in: https://console.cloud.google.com/apis/credentials/serviceaccountkey
* Do not forget to provide google storage access authorizations in your key.
* After creating your key, change the information in the "key_storage_credentials.json" file, according to the generated key.
* Define the storage bucket in Store() class instance, in this example, set in "server.py" file.
* Application is 8888 default port.

## Routes

| Metodo        | endpoint           | paramêtros  | descrição |
| ------------- |:------------------:| -----:| -----:|
| POST          |  `/api/v1/file/upload`  | {"base64": "...", "extension": "png/pdf/doc/txt ..."} | Upload file to bucket |
| DELETE          |  `/api/v1/file/remove/{file_name}`  | - | Romove file from bucket


## Português - BR

## Fluxo de funcionamento:
 
Para este exemplo, foi utilizado o framework http Tornado, para que possamos trafegar os dados base64 do cliente até este serviço.

Porém este serviço pode ser adaptado para qualquer API REST ou outros serviços HTTP desenvolvidos em Python.

* Crie sua chave de acesso em: https://console.cloud.google.com/apis/credentials/serviceaccountkey
* Não se esqueça de fornecer as autorizações necessárias a sua chave.
* Apos cria-la, substitua as informações no arquivo "key_storage_credentials.json", de acordo com a chave gerada.
* Define o storage bucket na instancia da classe Store(), neste exemplo você pode fazer isto no arquivo "server.py"

## Rotas

| Metodo        | endpoint           | paramêtros  | descrição |
| ------------- |:------------------:| -----:| -----:|
| POST          |  `/api/v1/file/upload`  | {"base64": "...", "extension": "png/pdf/doc/txt ..."} | Fazer upload de um novo arquivo |
| DELETE          |  `/api/v1/file/remove/{file_name}`  | - | Remover um arquivo do bucket |

