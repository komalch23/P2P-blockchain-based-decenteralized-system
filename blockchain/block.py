import time
from hashlib import sha256


class MyBlock(obj):

    def __init__(
            self, Id=0, nonce=0, LastHash=None, Record=None, CurrentHash=None,
            timestamp=None):
        self.Id = Id
        self.LastHash = LastHash or '0'
        self.timestamp = timestamp or time.time()
        self.Record = Record or ''
        self.nonce = nonce
        self.CurrentHash = CurrentHash or self.HashCompute()

    def to_dict(self):
        return {
            'Id': self.Id,
            'LastHash': self.LastHash,
            'timestamp': self.timestamp,
            'Record': self.Record,
            'nonce': self.nonce,
            'CurrentHash': self.CurrentHash
        }

    @staticmethod
    def gen():
        return MyBlock(
            0, 0, '0', 'Welcome to blockchain cli!',
            '8724f78170aee146b794ca6ad451d23c254717727e18e2b9643b81d5666aa908',
            1520572079.336289)

    def HashCompute(self):
        original_str = ''.join([
            str(self.Id), self.LastHash, str(self.timestamp), self.Record,
            str(self.nonce)])
        return sha256(original_str.encode('utf-8')).hexdigest()

    def __eq__(self, other):
        if (self.Id == other.Id
                and self.LastHash == other.LastHash
                and self.timestamp == other.timestamp
                and self.Record == other.Record
                and self.nonce == other.nonce
                and self.CurrentHash == other.CurrentHash):
            return True
        return False
