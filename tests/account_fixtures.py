import pytest

from nebpy.utils.crypto import Crypto


@pytest.fixture
def privkey_hex():
    return '01802530e353be5e92afb44f3dff6cef9d765133e86013893a0dad9c5663778f'


@pytest.fixture
def privkey_bytes(privkey_hex):
    return bytes.fromhex(privkey_hex)


@pytest.fixture
def public_key(privkey_bytes):
    return Crypto.private_to_public(privkey_bytes)


@pytest.fixture
def address():
    return b'\x19Wb\xc6<\xeeg\x1bam\xaa7}\xd3\xda\xdb\x1d\x18\x91\xdbwp"$\xe2\xac'  # noqa


@pytest.fixture
def verbose_address():
    return 'n1PX812RocrhGzoeFECXvKK9T168f8tUBa3'


@pytest.fixture
def invalid_verbose_address():
    return 'n1PX812RJcrhGzoeFECXvKK9T168f8tUBa3'
