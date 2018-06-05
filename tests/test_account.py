from nebpy.account import Account


class TestAccount:
    def test_compare_accounts(
            self, account_from_privkey_bytes, account_from_privkey_hex):
        assert (account_from_privkey_bytes.private_key ==
                account_from_privkey_hex.private_key)
        assert (account_from_privkey_bytes.public_key ==
                account_from_privkey_hex.public_key)

    def test_address(self, account_from_privkey_hex):
        address = b'\x19Wo\x82k\r\xd8F\x1b@-\xee\x86n\xb2u\xf8\xcdk/,\x9e\xb1\xa2\xf6\xef'  # noqa
        address_hex = '19576f826b0dd8461b402dee866eb275f8cd6b2f2c9eb1a2f6ef'
        address_base58 = b'n1QgTYKChKZqB5TtyeVUktnQfsoUL4fi3Wn'
        assert account_from_privkey_hex.address == address
        assert account_from_privkey_hex.address_hex == address_hex
        assert account_from_privkey_hex.address_base58 == address_base58

    def test_verbose_address(self, account_from_privkey_hex, verbose_address):
        assert account_from_privkey_hex.get_verbose_address() == verbose_address

    def test_check_is_valid_address(
            self, verbose_address, invalid_verbose_address):
        assert Account.check_is_valid_address(verbose_address)
        assert not Account.check_is_valid_address(invalid_verbose_address)
