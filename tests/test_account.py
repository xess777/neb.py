from nebpy.account import Account
from nebpy.utils.crypto import Crypto


class TestAccount:

    def test_init(self, privkey_hex, privkey_bytes, public_key, address):
        account = Account(privkey_hex)
        assert account.private_key == privkey_bytes
        assert account.public_key == public_key
        assert account.address == address

    def test_new_account(self):
        account = Account.new_account()
        public_key = Crypto.private_to_public(account.get_private_key())
        assert isinstance(account, Account)
        assert account.get_public_key() == public_key

    def test_set_private_key(self, privkey_hex, public_key, address):
        account = Account.new_account()
        account.set_private_key(privkey_hex)
        assert account.get_public_key() == public_key
        assert account.get_address() == address

    def test_verify_address(self, verbose_address, invalid_verbose_address):
        assert Account.verify_address(verbose_address)
        assert not Account.verify_address(invalid_verbose_address)

    def test_get_verbose_address(self, privkey_hex, verbose_address):
        account = Account(privkey_hex)
        assert account.get_verbose_address() == verbose_address

    def from_key(self):
        pass

    def test_to_key(self):
        pass
