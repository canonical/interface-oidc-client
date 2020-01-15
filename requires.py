import json

from charms.reactive import Endpoint, toggle_flag


class OidcClientRequirer(Endpoint):
    def manage_flags(self):
        toggle_flag(
            self.expand_name('{endpoint_name}.available'),
            self.is_joined and 'client_info' in self.all_joined_units.received_raw)

    def get_config(self):
        return [
            json.loads(unit.received_raw["client_info"])
            for relation in self.relations
            for unit in relation.joined_units
        ]
