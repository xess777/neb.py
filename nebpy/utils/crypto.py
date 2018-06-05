from ecdsa import SigningKey, SECP256k1


class Crypto(object):
    @staticmethod
    def create_private_key():
        sk = SigningKey.generate(curve=SECP256k1)
        private_key = sk.to_string()

        return private_key

    @staticmethod
    def private_to_public(private_key):
        sk = SigningKey.from_string(private_key, curve=SECP256k1)
        vk = sk.get_verifying_key()
        public_key = vk.to_string()

        return public_key
