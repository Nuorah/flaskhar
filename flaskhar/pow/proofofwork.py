import hashlib

max_nonce = 2 ** 32

def find_nonce(block, difficulty_bits):
    for nonce in range(max_nonce):
        if (test_nonce(nonce, block, difficulty_bits)[0]):
            return (nonce, test_nonce(nonce, block, difficulty_bits)[1])
    return nonce

def test_nonce(nonce, block, difficulty_bits):
    target = 2 ** (256 - difficulty_bits)
    hash_result = hashlib.sha256((str(nonce) + str(block)).encode()).hexdigest()
    return (int(hash_result, 16) < target, hash_result)



