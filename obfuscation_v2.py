# obfuscation.py

import base64
import random
import string
import argparse
import os

def random_var(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def xor_encrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def obfuscate(code, filename):
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(4, 10)))
    xored = xor_encrypt(code, key)
    b64_encoded = base64.b64encode(xored.encode()).decode()

    # Variáveis randômicas
    xor_fn = random_var()
    key_var = random_var()
    code_var = random_var()
    temp_var = random_var()

    obfuscated_code = f'''
# Arquivo ofuscado automaticamente de: {filename}
import base64 as b64

def {xor_fn}(data, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

{key_var} = "{key}"
{code_var} = "{b64_encoded}"
{temp_var} = b64.b64decode({code_var}).decode()
exec({xor_fn}({temp_var}, {key_var}))
'''
    return obfuscated_code

def main():
    parser = argparse.ArgumentParser(description="Polymorphic XOR Obfuscator")
    parser.add_argument("input", help="Arquivo Python a ser ofuscado (ex: teste.py)")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"[-] Arquivo não encontrado: {args.input}")
        return

    with open(args.input, 'r', encoding='utf-8') as f:
        code = f.read()

    filename = os.path.basename(args.input)
    output_file = f'obf_{filename}'

    obfuscated = obfuscate(code, filename)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(obfuscated)

    print(f"[+] Arquivo ofuscado gerado: {output_file}")

if __name__ == "__main__":
    main()
