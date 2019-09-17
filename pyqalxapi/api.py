import os
from . import request
import json

class API() :
    def __init__(self, **kw):
        self.baseurl = 'https://api.qalx.io/'
        self.headers = {'Authorization': 'Token {0}'.format(kw['token'])}
        self.request = request.RequestHandler()


    def get(self, entity, **kwargs):
        params = {}
        url = "{0}/{1}".format(self.baseurl.strip('/'), '{0}'.format(entity))
        if 'params' in kwargs:
            params.update(kwargs['params'])
        return self.request.make_request(method='GET', url=url, params=params, headers=self.headers)

    def post(self, entity, **kwargs):
        url = "{0}/{1}".format(self.baseurl.strip('/'), '{0}'.format(entity))
        if 'file' in kwargs:
            if os.path.isfile(str(kwargs['file'])):
                file_path = os.path.abspath(kwargs['file'])
                folder, file_name = os.path.split(file_path)
                size = os.path.getsize(kwargs['file'])
                kwargs['file'] = {'name':file_name, 'size': size}
        save_file = self.request.make_request(method='POST', params=kwargs, url=url, headers=self.headers)
        if ('upload' not in kwargs or kwargs['upload']) and 'file_path' in locals() and save_file.ok:
            return self.upload_to_s3(save_file.json(), file_path)
        return save_file

    def upload_to_s3(self, response, file_path):
        url = response['file']['url']
        return self.request.make_request(method='PUT', file=file_path, url=url)

    def patch(self, entity, **kwargs):
        url = "{0}/{1}".format(self.baseurl.strip('/'), entity)
        return self.request.make_request(method='PATCH', url=url, params=kwargs, headers=self.headers)

    def delete(self, entity):
        url = "{0}/{1}".format(self.baseurl.strip('/'), entity)
        return self.request.make_request(method='DELETE', url=url, headers=self.headers)
