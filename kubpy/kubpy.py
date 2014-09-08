import json
import requests

from requests.auth import HTTPBasicAuth


class KubPy(object):
    def __init__(self, base_url, username, password):
        if not base_url.endswith('/'):
            base_url += '/'
        self.base_url = base_url
        self.auth = HTTPBasicAuth(username, password)

    def send_request(self, method, path, labels=None, body=None):
        url = self.base_url + path
        kwargs = {'auth': self.auth, 'verify': False}
        if body:
            kwargs['body'] = json.dumps(body)
        if labels:
            path += '?labels='
            for key, value in labels.iteritems():
                path += '{}={}'.format(key, value)
        resp = getattr(requests, method)(url, **kwargs)
        resp = resp.json()
        return resp

    # Minions
    def list_minions(self, labels=None):
        return self.send_request('get', 'minions', labels)

    def get_minion(self, id):
        return self.send_request('get', 'minions/{}'.format(id))

    # Pods
    def list_pods(self, labels=None):
        return self.send_request('get', 'pods', labels)

    def get_pod(self, id):
        return self.send_request('get', 'pods/{}'.format(id))
    
    def create_pod(self, body):
        return self.send_request('post', 'pods', body)

    def update_pod(self, body):
        return self.send_request('put', 'pods', body)
    
    def delete_pod(self, id):
        return self.send_request('delete', 'pods/{}'.format(id))
    
    # Replication Controllers
    def list_replication_controllers(self, labels=None):
        return self.send_request('get', 'replicationControllers', labels)

    def get_replication_controller(self, id):
        return self.send_request('get', 'replicationControllers/{}'.format(id))

    def create_replication_controller(self, body):
        return self.send_request('post', 'replicationControllers', body)

    def update_replication_controller(self, body):
        return self.send_request('put', 'replicationControllers', body)

    def delete_replication_controller(self, id):
        return self.send_request('delete',
                                 'replicationControllers/{}'.format(id))
    
    # Services
    def list_services(self, labels=None):
        return self.send_request('get', 'services', labels)

    def get_service(self, id):
        return self.send_request('get', 'services/{}'.format(id))

    def create_service(self, body):
        return self.send_request('post', 'services', body)

    def update_service(self, body):
        return self.send_request('put', 'services', body)

    def delete_service(self, id):
        return self.send_request('delete', 'services/{}'.format(id))
