from rest_framework.compat import yaml
from rest_framework.renderers import BaseRenderer

class OpenApiBaseAuth(BaseRenderer):
    media_type = 'text/plain'
    format = 'openapi'
    
    def render(self, data, accepted_media_type=None, renderer_context=None):
        class Dumper(yaml.Dumper):
            def ignore_aliases(self, data):
                return True
        data["security"] = [{"BasicAuth": []}]
        data["components"]["securitySchemes"] = {"BasicAuth": {"type": "http", "scheme": "basic"}}
        return yaml.dump(data, default_flow_style=False, sort_keys=False, Dumper=Dumper).encode('utf-8')