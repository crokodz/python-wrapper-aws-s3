import requests

class RequestHandler():
    def make_request(self, method, url, params={}, headers={}, file={}):
        if method == 'POST':
            try:
                return requests.request(url=url, method=method,
                                    json=params, headers=headers)
            except requests.exceptions.HTTPError as err:
                return err
        elif method == 'GET':
            try:
                return requests.request(url=url, method=method, params=params,
                                    headers=headers)
            except requests.exceptions.HTTPError as err:
                return err
        elif method == 'PUT':
            if file:
                try:
                    return requests.request(url=url, method=method,
                                         data=open(file).read())
                except requests.exceptions.HTTPError as err:
                    return err
        elif method == 'PATCH':
            try:
                return requests.request(url=url, method=method, json=params,
                                    headers=headers)
            except requests.exceptions.HTTPError as err:
                return err
        elif method == 'DELETE':
            try:
                return requests.request(url=url, method=method,
                                    headers=headers)
            except requests.exceptions.HTTPError as err:
                return err