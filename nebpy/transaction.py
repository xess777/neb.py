class Transaction(object):
    """Class encapsulate main operation with transactions.
    """
    def hash_transaction(self):
        """Convert transaction to hash by SHA3-256 algorithm."""

    def signTransaction(self):
        """Sign transaction with the specified algorithm."""

    def to_dict(self):
        """Convert transaction data to dict"""

    def to_json(self):
        """Convert transaction to JSON string."""

    def to_proto(self):
        """Convert transaction to Protobuf format."""

    def to_proto_str(self):
        """Convert transaction to Protobuf hash string."""

    def from_proto(self, data):
        """Restore Transaction from Protobuf format."""

