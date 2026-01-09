from string import punctuation, digits, ascii_letters

CHARS = " " + punctuation + digits + ascii_letters
CHARS = list(CHARS)

def decrypt_password(encrypted_password: str, stored_key: str) -> str:
    key = list(stored_key)
    decrypted = ""

    for char in encrypted_password:
        decrypted += CHARS[key.index(char)]

    return decrypted


# -------- YOUR DB VALUES --------

encrypted_password = "^39b#@GB"
hash_key = """+"Acu4OCHw1kE8RjZh&oe){WY?z.t5*='7@GBKp}L-U^<23V/v!b D(9#y>qixnfF_ITMa6`,g:;$0sXP[]dSQm~|N\Jl%r"""

# -------- DECRYPT --------

plain_password = decrypt_password(encrypted_password, hash_key)
print("Decrypted password:", plain_password)