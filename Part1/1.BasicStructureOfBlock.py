
"""

Each block has an index, a timestamp (in Unix time), a list of transactions,
a proof , and the hash of the previous block. Each new block contains
within itself, the hash of the previous Block. This is crucial because it's
what gives blockchains immutability: If an attacker corrupted an earlier
Block in the chain then all subsequent blocks will contain incorrect hashes.

"""

block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
