import yaml
from openapi3 import OpenAPI
from config import settings
import requests
from requests.auth import HTTPBasicAuth


def create_reader():
    basic = HTTPBasicAuth(settings.api_user, settings.api_password)
    res = requests.get(f'{settings.api_url}/openapi/', auth=basic)
    if res.status_code != 200:
        raise requests.exceptions.HTTPError
    api_yaml = yaml.safe_load(res.text)
    api_yaml['servers'] = [{'url': settings.api_url.__str__()}]
    return OpenAPI(api_yaml)


api_io = create_reader()
api_io.authenticate('BasicAuth', (settings.api_user, settings.api_password))
