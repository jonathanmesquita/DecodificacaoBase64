import base64

# Codificado em Base64
encoded = "dXN1YXJpbzpzZW5oYTEyMw=="

# Decodificando
decoded = base64.b64decode(encoded).decode('utf-8')

print(decoded)
