from http import HTTPStatus
from base64_handler import decode_b64_to_file
from storage import Storage

import tornado.ioloop
import tornado.web
import json
import logging


class UploadFile(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        try:
            file_name = decode_b64_to_file(b64=data.get('base64'), extension=data.get('extension'))
            result = self.settings['storage'].upload_to_bucket(blob_name=file_name)
        except Exception as ex:
            logging.error(ex)
            self.set_status(500)
            self.finish({'message': str(ex)})
            raise ex
        else:
            self.set_status(HTTPStatus.CREATED)
            self.finish(result)


class RemoveFile(tornado.web.RequestHandler):
    def delete(self, file_name):
        try:
            result = self.settings['storage'].remove_from_bucket(file_name)
        except Exception as ex:
            logging.error(ex)
            self.set_status(500)
            self.finish({'message': str(ex)})
        else:
            self.set_status(HTTPStatus.OK)
            self.finish(result)


def make_app():
    return tornado.web.Application([
        (r"/api/v1/file/upload", UploadFile),
        (r"/api/v1/file/remove/?(.*)?", RemoveFile),
    ], storage=Storage(bucket_name='storage-hub'))


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print('Service is running in {} port.'.format(8888))
    tornado.ioloop.IOLoop.current().start()
