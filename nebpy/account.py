import base58

from nebpy.helpers import int_to_bytes, sha3_256, ripemd160
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
        :param private_key: hex string
        """
        if private_key is None:
            self.private_key = Crypto.create_private_key()
            self.private_key_hex = self.private_key.hex()
        elif isinstance(private_key, str):
            self.private_key_hex = private_key
            self.private_key = bytes.fromhex(self.private_key_hex)
        elif isinstance(private_key, bytes):
            self.private_key = private_key
            self.private_key_hex = self.private_key.hex()

        self.public_key = Crypto.private_to_public(self.private_key)
        self.public_key_hex = self.public_key.hex()
        self.address = self.address_from_public_key()
        self.address_hex = self.address.hex()
        self.address_base58 = base58.b58encode(self.address)

    @classmethod
    def check_is_valid_address(cls, address, address_type=None):
        """
        Validate address.
        :param address: base58 encode address
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

    def address_from_public_key(self):
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

    def get_verbose_address(self):
        return self.address_base58.decode()
