import hashlib


def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) >> 3, 'big')


def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big')


def sha3_256(content):
    h = hashlib.new('sha3_256')
    h.update(content)

    return h.digest()


def ripemd160(content):
    h = hashlib.new('ripemd160')
    h.update(content)

    return h.digest()
