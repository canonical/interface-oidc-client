import json

from charms.reactive import Endpoint, toggle_flag


class OidcClientRequirer(Endpoint):
    def manage_flags(self):
        toggle_flag(
            self.expand_name('{endpoint_name}.available'),
            self.is_joined and 'client_info' in self.all_joined_units.received_raw)

    def get_config(self):
        return [
            json.loads(relation.joined_units.received_raw["client_info"])
            for relation in self.relations
            if relation.joined_units.received_raw.get('client_info')
        ]
