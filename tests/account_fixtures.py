import pytest

from nebpy.account import Account


@pytest.fixture
def privkey_bytes():
    return b'\xca9\x12{\x81\xeb2\x0eIZ\\\x96$\xad\xa3\xf7\xda\x9aU\xd5W\xf3\x92\xadc|\x12\xc0\x84\x90\xe1\x9a'  # noqa


@pytest.fixture
def privkey_hex():
    return 'ca39127b81eb320e495a5c9624ada3f7da9a55d557f392ad637c12c08490e19a'


@pytest.fixture
def account_from_privkey_bytes(privkey_bytes):
    return Account(privkey_bytes)


@pytest.fixture
def account_from_privkey_hex(privkey_hex):
    return Account(privkey_hex)


@pytest.fixture
def verbose_address():
    return 'n1QgTYKChKZqB5TtyeVUktnQfsoUL4fi3Wn'


@pytest.fixture
def invalid_verbose_address():
    return 'n1QgTYKChKZqB5TtyeVUktnQfsoUL5fi3Wn'
