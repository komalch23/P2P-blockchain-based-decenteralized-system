from blockchain.Block import MyBlock


class MyChain(object):

    def __init__(self):
        genesis = MyBlock.genesis()
        self._Record_list = [genesis]
        self._difficulty = 4

    def mine(self, Record):
        Last = self._latest_block
        nonce = 0
        while True:
            nonce += 1
            new = MyBlock(Last.Id + 1, nonce, Last.CurrentHash, Record)
            if self.check_hash_valid(new.CurrentHash):
                self._Record_list.append(new)
                break

    def replace_chain(self, MyChain):
        if len(MyChain) > len(self._Record_list):
            Record_list = []
            for Block in MyChain:
                Record_list.append(MyBlock(
                    int(Block['Id']), int(Block['nonce']),
                    Block['LastHash'], Block['Record'], Block['CurrentHash'],
                    float(Block['timestamp'])))
            self._Record_list = Record_list

    def to_dict(self):
        return [item.to_dict() for item in self._Record_list]

    def check_hash_valid(self, CurrentHash):
        return CurrentHash[:self._difficulty] == '0' * self._difficulty

    @property
    def _latest_block(self):
        return self._Record_list[-1]
