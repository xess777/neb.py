import base58

from nebpy.helpers import sha3_256, ripemd160
from nebpy.utils.crypto import Crypto


class Account(object):
    """Class encapsulate main operation with account entity.
    """
    ADDRESS_LENGTH = 26
    ADDRESS_PREFIX = b'\x19'
    NORMAL_TYPE = b'W'
    CONTRACT_TYPE = b'X'

    def __init__(self, private_key=None):
        """
        :param private_key: hex string or bytes
        """
        if private_key is None:
            self.private_key = Crypto.create_private_key()
        elif isinstance(private_key, str):
            self.private_key = bytes.fromhex(private_key)
        elif isinstance(private_key, bytes):
            self.private_key = private_key

        self.public_key = Crypto.private_to_public(self.private_key)
        self.address = self._address_from_public_key()

    @classmethod
    def new_account(cls):
        """
        Account factory method.
        Create random account.
        :return: Instance of Account constructor.
        :rtype: Account
        """
        return cls()

    @classmethod
    def from_key(cls, key, passphrase):
        """
        Restore account from key and passphrase.
        :param key: Key Object.
        :param passphrase: Provided password.
        :return: Instance of Account restored from key and passphrase.
        :rtype: Account
        """

    @classmethod
    def verify_address(cls, address, address_type=None):
        """
        :param address: base58 encode address
        :type address: str
        :param address_type: normal or smart contract type
        :type address_type: bytes
        :return: flag is address valid
        :rtype: bool
        """
        if not address or not isinstance(address, str):
            return False
        address = base58.b58decode(address)
        if len(address) != cls.ADDRESS_LENGTH:
            return False
        if address[:1] != cls.ADDRESS_PREFIX:
            return False
        type_ = address[1:2]
        if address_type is not None:
            if type_ != address_type:
                return False
        elif type_ not in [cls.NORMAL_TYPE, cls.CONTRACT_TYPE]:
            return False
        content = address[0:22]
        checksum = address[-4:]
        result = sha3_256(content)[0:4] == checksum

        return result

    def set_private_key(self, private_key_hex):
        """
        Private Key setter.
        :param private_key: Account private key (hex string).
        :type private_key: str
        """
        self.private_key = bytes.fromhex(private_key_hex)
        self.public_key = Crypto.private_to_public(self.private_key)
        self.address = self._address_from_public_key()

    def get_private_key(self):
        """
        Private Key getter.
        :return: Account private key.
        :rtype: bytes
        """
        return self.private_key

    def get_public_key(self):
        """
        Public Key getter.
        :return: Account public key.
        :rtype: bytes
        """
        return self.public_key

    def get_public_key_hex(self):
        """
        Get Public Key in hex string format.
        :return: Account public key in hex string format.
        :rtype: str
        """
        return self.get_public_key().hex()

    def get_address(self):
        """
        Accaunt address getter.
        :return: Account address.
        :rtype: bytes
        """
        return self.address

    def get_address_hex(self):
        """
        Get account address in hex string format.
        :return: Account address in hex string format.
        :rtype: str
        """
        return self.get_address().hex()

    def get_verbose_address(self):
        """
        Get verbose account address.
        :return: Account address in base58 encode format.
        :rtype: str
        """
        return base58.b58encode(self.get_address()).decode()

    def to_key(self, passphrase, opts):
        """
        Generate key buy passphrase and options.
        :param passphrase: Provided password.
        :param opts: Key options.
        :return: Key Object.
        """

    def to_key_json(self, passphrase, opts):
        """
        Generate key buy passphrase and options.
        Return in JSON format.
        :param passphrase: Provided password.
        :param opts: Key options.
        :return: JSON stringify Key.
        """

    def _address_from_public_key(self):
        """
        :return: Address
        :rtype: bytes
        """
        content = b'\x04' + self.public_key
        content = sha3_256(content)
        content = ripemd160(content)
        content = self.ADDRESS_PREFIX + self.NORMAL_TYPE + content
        checksum = sha3_256(content)[0:4]
        address = content + checksum

        return address
