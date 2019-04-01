import kerberos
import pytest

from web_service import create_app


@pytest.fixture
def client():
    client = create_app()
    return client.test_client()


def test_auth(client):
    hostname = "kerberos.example.com"
    service = f"HTTP@{hostname}"
    mech_oid = kerberos.GSS_MECH_OID_KRB5
    rc, vc = kerberos.authGSSClientInit(service=service, mech_oid=mech_oid)
    kerberos.authGSSClientStep(vc, "")
    kerberos_token = kerberos.authGSSClientResponse(vc)
    headers = {"Authorization": f"Negotiate {kerberos_token}"}
    r = client.get("/", headers=headers)
    assert r.status_code == 200
