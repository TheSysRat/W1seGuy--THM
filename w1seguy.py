import binascii

def xor_decrypt(hex_string, key):
    # Convert the hex string to bytes
    encrypted_bytes = binascii.unhexlify(hex_string)
    
    # Repeat the key to match the length of the encrypted bytes
    repeated_key = (key * (len(encrypted_bytes) // len(key) + 1))[:len(encrypted_bytes)]
    
    # Perform XOR between each byte of the encrypted bytes and the key
    decrypted_bytes = bytes([b ^ ord(repeated_key[i]) for i, b in enumerate(encrypted_bytes)])
    
    # Convert bytes to string
    decrypted_message = decrypted_bytes.decode('utf-8')
    
    return decrypted_message

# Given XOR-encoded message
hex_encoded_message = input('Tell me hex to brute-forcing >> ')

# Convert hex string to bytes
encrypted_bytes = binascii.unhexlify(hex_encoded_message)

# Known plaintext (first few characters of the flag and the last character)
known_plaintext_start = "THM{"
known_plaintext_end = "}"

# Determine key using known plaintext start
key = [encrypted_bytes[i] ^ ord(known_plaintext_start[i]) for i in range(len(known_plaintext_start))]

# Determine key using known plaintext end
for i in range(1, len(known_plaintext_end) + 1):
    key.append(encrypted_bytes[-i] ^ ord(known_plaintext_end[-i]))

# Convert key to string
key = ''.join([chr(k) for k in key[:5]])

# Decrypt the message
decrypted_message = xor_decrypt(hex_encoded_message, key)
print(f"Decrypted message: {decrypted_message}")
print(f"Encryption key: {key}")
