import json

from charms.reactive import Endpoint, toggle_flag


class OidcClientProvider(Endpoint):
    def manage_flags(self):
        toggle_flag(self.expand_name('{endpoint_name}.available'), self.is_joined)

    def configure(self, connection_info):
        for relation in self.relations:
            relation.to_publish_raw['client_info'] = json.dumps(connection_info)
