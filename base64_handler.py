import base64
import uuid


def decode_b64_to_file(b64, extension, name=None):
    if not name:
        name = uuid.uuid4().hex

    with open("{}.{}".format(name, extension), "wb") as fh:
        try:
            fh.write(base64.decodebytes(b64.encode()))
        except Exception as ex:
            raise ex
        else:
            return fh.name
