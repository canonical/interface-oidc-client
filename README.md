interface-oidc-client
=====================

Adds an interface to Juju for OIDC clients to send client information to an
OIDC server.


Example Usage
-------------

In the client charm, add a section like this to `metadata.yaml`:

```yaml
provides:
  oidc-client:
    interface: oidc-client
```

Then, in the charm itself, send client information like this:

```python
@when('oidc-client.available')
def configure_oidc(oidc):
    oidc.configure(
        {
            'id': hookenv.config('client-id'),
            'name': hookenv.config('client-name'),
            'redirectURIs': [hookenv.config('public-url') + '/oidc/login/oidc'],
            'secret': hookenv.config('client-secret'),
        }
    )
```

Finally, in the server charm, access the client config like this:

```python
@when("oidc-client.available", ...)
@when_not("charm.started")
def start_charm():
    ...
    oidc_client_info = endpoint_from_name('oidc-client').get_config()
```
