from google.cloud import storage

import logging
import os


class Storage:

    def __init__(self, bucket_name):
        try:
            self.storage_client = storage.Client.from_service_account_json(
                'key_storage_credentials.json')
            self.bucket = self.storage_client.get_bucket(bucket_name)
        except Exception as ex:
            logging.exception(ex)
            raise ex

    def upload_to_bucket(self, blob_name):
        path_to_file = blob_name
        try:
            blob = self.bucket.blob(blob_name)
            blob.upload_from_filename(path_to_file)
        except Exception as ex:
            raise ex
        else:
            os.remove(path_to_file)
            return {
                'file_name': blob_name,
                'url': blob.public_url,
                'size': blob.size
            }

    def remove_from_bucket(self, file_name):
        try:
            teste = self.bucket.delete_blob(blob_name=file_name)
            print(teste)
        except Exception as ex:
            logging.exception(ex)
            raise ex
        else:
            return {'message': 'sucess in delete {} file.'.format(file_name)}
